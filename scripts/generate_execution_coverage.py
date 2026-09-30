"""Create deterministic, portable SQLite coverage examples for the V1 gate.

The generated cases are small semantic checks, not benchmark claims. They are
declared YAML examples and must be executed by sql_harness.py before they can
contribute to release metrics.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import yaml

try:
    from .kb_core import ROOT, load_yaml
except ImportError:
    from kb_core import ROOT, load_yaml


def existing_example_documents(root: Path) -> list[str]:
    ids: list[str] = []
    for path in sorted((root / "examples").rglob("SQL-*.yaml")):
        value = load_yaml(path)
        if value.get("document_id"):
            ids.append(str(value["document_id"]))
    return sorted(set(ids))


def case(number: int, document_id: str) -> dict:
    table = f"coverage_{number}"
    mode = number % 10
    if mode == 0:
        statement = f"SELECT {number} AS case_id"
        setup: list[str] = []
        expectation = {"rows": [[number]]}
    elif mode == 1:
        setup = [f"CREATE TABLE {table} (v INTEGER); INSERT INTO {table} VALUES ({number}), ({number + 1});"]
        statement = f"SELECT COUNT(*), SUM(v) FROM {table}"
        expectation = {"rows": [[2, number * 2 + 1]]}
    elif mode == 2:
        setup = [f"CREATE TABLE {table} (v INTEGER); INSERT INTO {table} VALUES ({number}), ({number + 1}), ({number + 2});"]
        statement = f"SELECT v FROM {table} WHERE v % 2 = 0 ORDER BY v"
        expected = [[number], [number + 2]] if number % 2 == 0 else [[number + 1]]
        expectation = {"rows": expected}
    elif mode == 3:
        setup = [f"CREATE TABLE {table} (grp TEXT, v INTEGER); INSERT INTO {table} VALUES ('a', {number}), ('a', {number + 1}), ('b', {number + 2});"]
        statement = f"SELECT grp, COUNT(*), SUM(v) FROM {table} GROUP BY grp ORDER BY grp"
        expectation = {"rows": [["a", 2, number * 2 + 1], ["b", 1, number + 2]]}
    elif mode == 4:
        setup = [f"CREATE TABLE {table} (id INTEGER PRIMARY KEY, label TEXT); INSERT INTO {table} VALUES ({number}, 'x');"]
        statement = f"SELECT id, UPPER(label) FROM {table}"
        expectation = {"rows": [[number, "X"]]}
    elif mode == 5:
        setup = [f"CREATE TABLE {table} (v INTEGER); INSERT INTO {table} VALUES ({number}), (NULL);"]
        statement = f"SELECT COUNT(v), COUNT(*) FROM {table}"
        expectation = {"rows": [[1, 2]]}
    elif mode == 6:
        statement = f"SELECT CASE WHEN {number} > 0 THEN 'positive' ELSE 'non-positive' END"
        setup = []
        expectation = {"rows": [["positive"]]}
    elif mode == 7:
        statement = f"WITH nums(v) AS (VALUES ({number}), ({number + 1})) SELECT SUM(v) FROM nums"
        setup = []
        expectation = {"rows": [[number * 2 + 1]]}
    elif mode == 8:
        setup = [f"CREATE TABLE {table} (v INTEGER); INSERT INTO {table} VALUES ({number}), ({number + 1}), ({number + 2});"]
        statement = f"SELECT v, ROW_NUMBER() OVER (ORDER BY v) FROM {table} ORDER BY v"
        expectation = {"rows": [[number, 1], [number + 1, 2], [number + 2, 3]]}
    else:
        setup = [f"CREATE TABLE {table} (v INTEGER CHECK (v >= 0)); INSERT INTO {table} VALUES ({number});"]
        statement = f"SELECT v * 2 FROM {table}"
        expectation = {"rows": [[number * 2]]}
    return {
        "schema_version": 1,
        "id": f"SQL-GC-{number:04d}",
        "document_id": document_id,
        "dialect": "portable",
        "environment": "sqlite-local",
        "setup": setup,
        "statement": statement,
        "expectation": expectation,
    }


def generate(root: Path, count: int) -> None:
    documents = existing_example_documents(root)
    if not documents:
        raise RuntimeError("no existing executable document IDs found")
    target = root / "examples" / "generated-coverage"
    target.mkdir(parents=True, exist_ok=True)
    for number in range(1, count + 1):
        value = case(number, documents[(number - 1) % len(documents)])
        (target / f"{value['id']}.yaml").write_text(
            yaml.safe_dump(value, sort_keys=False, allow_unicode=True), encoding="utf-8"
        )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, default=911)
    args = parser.parse_args()
    generate(ROOT, args.count)
    print(f"generated {args.count} deterministic coverage examples")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
