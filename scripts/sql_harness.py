from __future__ import annotations

import argparse
import hashlib
import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator, FormatChecker

try:
    from .kb_core import ROOT, load_json, load_yaml
except ImportError:  # direct script execution
    from kb_core import ROOT, load_json, load_yaml


def normalize_rows(rows: list[tuple[Any, ...]]) -> list[list[Any]]:
    return [list(row) for row in rows]


def evidence_base(example: dict[str, Any]) -> dict[str, Any]:
    statement = example["statement"]
    return {
        "schema_version": 1,
        "example_id": example["id"],
        "document_id": example["document_id"],
        "environment": example["environment"],
        "engine": "sqlite" if example["environment"] == "sqlite-local" else example["dialect"],
        "engine_version": sqlite3.sqlite_version if example["environment"] == "sqlite-local" else "UNAVAILABLE",
        "executed_at": datetime.now(timezone.utc).isoformat(),
        "statement_sha256": hashlib.sha256(statement.encode("utf-8")).hexdigest(),
    }


def execute_sqlite(example: dict[str, Any], allow_destructive: bool = False) -> dict[str, Any]:
    evidence = evidence_base(example)
    if example.get("destructive") and not allow_destructive:
        evidence.update(status="BLOCKED", message="destructive example requires explicit opt-in")
        return evidence
    connection = sqlite3.connect(":memory:")
    try:
        for statement in example["setup"]:
            connection.executescript(statement)
        try:
            cursor = connection.execute(example["statement"])
            rows = normalize_rows(cursor.fetchall())
            expectation = example["expectation"]
            if "error_class" in expectation:
                evidence.update(
                    status="FAIL",
                    actual_rows=rows,
                    message=f"expected error {expectation['error_class']}, statement succeeded",
                )
            elif rows == expectation["rows"]:
                evidence.update(status="PASS", actual_rows=rows)
            else:
                evidence.update(
                    status="FAIL",
                    actual_rows=rows,
                    message=f"expected rows {expectation['rows']!r}",
                )
        except sqlite3.Error as exc:
            expectation = example["expectation"]
            error_class = type(exc).__name__
            if "error_class" in expectation:
                message_matches = expectation.get("message_contains", "") in str(exc)
                class_matches = expectation["error_class"] == error_class
                after_matches = True
                after_rows: list[list[Any]] | None = None
                if "after_error" in expectation:
                    connection.rollback()
                    after_rows = normalize_rows(
                        connection.execute(expectation["after_error"]["statement"]).fetchall()
                    )
                    after_matches = after_rows == expectation["after_error"]["rows"]
                evidence.update(
                    status="PASS" if class_matches and message_matches and after_matches else "FAIL",
                    actual_error_class=error_class,
                    message=str(exc),
                )
                if after_rows is not None:
                    evidence["actual_rows"] = after_rows
            else:
                evidence.update(status="FAIL", actual_error_class=error_class, message=str(exc))
    finally:
        connection.close()
    return evidence


def run_example(
    path: Path, environments: dict[str, Any], allow_destructive: bool = False
) -> dict[str, Any]:
    example = load_yaml(path)
    validator = Draft202012Validator(
        load_json(ROOT / "schemas" / "sql-example.schema.json"), format_checker=FormatChecker()
    )
    validator.validate(example)
    environment = environments[example["environment"]]
    if not environment["available"]:
        evidence = evidence_base(example)
        evidence.update(status="NOT_RUN", message=environment["blocked_reason"])
        return evidence
    if example["environment"] == "sqlite-local":
        return execute_sqlite(example, allow_destructive=allow_destructive)
    evidence = evidence_base(example)
    evidence.update(status="BLOCKED", message="configured engine adapter is not implemented")
    return evidence


def main() -> int:
    parser = argparse.ArgumentParser(description="Run declared SQL examples and store evidence")
    parser.add_argument("paths", nargs="*", type=Path)
    parser.add_argument("--no-write", action="store_true")
    parser.add_argument(
        "--allow-destructive",
        action="store_true",
        help="run examples marked destructive; environments must still be isolated",
    )
    args = parser.parse_args()
    config = load_yaml(ROOT / "examples" / "environments.yaml")
    environments = config["environments"]
    paths = args.paths or sorted((ROOT / "examples").rglob("SQL-*.yaml"))
    output_dir = ROOT / "validation" / "execution"
    output_dir.mkdir(parents=True, exist_ok=True)
    failed = False
    for candidate in paths:
        path = candidate if candidate.is_absolute() else ROOT / candidate
        evidence = run_example(path, environments, allow_destructive=args.allow_destructive)
        if not args.no_write:
            target = output_dir / f"{evidence['example_id']}.json"
            target.write_text(json.dumps(evidence, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"{evidence['example_id']}: {evidence['status']}")
        failed = failed or evidence["status"] == "FAIL"
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
