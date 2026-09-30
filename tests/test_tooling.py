from __future__ import annotations

import json
from pathlib import Path

import pytest
import yaml

from scripts.atlas_validate import EXPECTED_COUNTS, validate_atlas
from scripts.docmost_bundle import build_bundle
from scripts.docmost_adapter import plan_sync
from scripts.kb_core import (
    Document,
    anchors,
    parse_front_matter,
    prerequisite_cycles,
    qa_report,
)
from scripts.sql_harness import execute_sqlite, run_example


def test_front_matter_parser(tmp_path: Path):
    path = tmp_path / "document.md"
    path.write_text("---\nid: DBKB-FND-0001\n---\n# Cím\n", encoding="utf-8")
    document = parse_front_matter(path)
    assert document.metadata["id"] == "DBKB-FND-0001"
    assert document.body == "# Cím\n"


def test_front_matter_parser_rejects_plain_markdown(tmp_path: Path):
    path = tmp_path / "document.md"
    path.write_text("# Nincs metadata\n", encoding="utf-8")
    with pytest.raises(ValueError, match="missing YAML front matter"):
        parse_front_matter(path)


def test_anchor_generation_handles_duplicates_and_hungarian_text():
    assert anchors("# Árvíztűrő tükörfúrógép\n## Rész\n## Rész\n") == {
        "árvíztűrő-tükörfúrógép",
        "rész",
        "rész-1",
    }


def test_prerequisite_cycle_detection():
    root = Path("/repo")
    documents = [
        Document(root / "a.md", {"id": "A", "prerequisites": ["B"]}, ""),
        Document(root / "b.md", {"id": "B", "prerequisites": ["A"]}, ""),
    ]
    assert prerequisite_cycles(documents) == [["A", "B", "A"]]


def test_qa_report_is_stable_except_timestamp():
    first = qa_report([], "2026-01-01T00:00:00+00:00")
    second = qa_report([], "2026-01-02T00:00:00+00:00")
    assert first["run_id"] == second["run_id"]
    assert first["dimensions"]["release_gate"] == "PASS"


def test_atlas_tiny_fixture_executes_with_expected_integrity():
    result = validate_atlas()
    assert result["pass"] is True
    assert result["counts"] == EXPECTED_COUNTS
    assert result["foreign_key_violations"] == []
    assert result["order_5001_total"] == 160.0


def test_sql_harness_asserts_rows():
    evidence = execute_sqlite(
        {
            "schema_version": 1,
            "id": "SQL-FND-0001",
            "document_id": "DBKB-FND-0016",
            "dialect": "portable",
            "environment": "sqlite-local",
            "setup": ["CREATE TABLE t (v INTEGER); INSERT INTO t VALUES (1), (NULL);"],
            "statement": "SELECT COUNT(v), COUNT(*) FROM t",
            "expectation": {"rows": [[1, 2]]},
        }
    )
    assert evidence["status"] == "PASS"
    assert evidence["actual_rows"] == [[1, 2]]
    assert evidence["engine_version"] != "UNAVAILABLE"


def test_sql_harness_asserts_expected_error():
    evidence = execute_sqlite(
        {
            "schema_version": 1,
            "id": "SQL-FND-0002",
            "document_id": "DBKB-FND-0016",
            "dialect": "sqlite",
            "environment": "sqlite-local",
            "setup": [],
            "statement": "SELECT missing_column",
            "expectation": {
                "error_class": "OperationalError",
                "message_contains": "no such column",
            },
        }
    )
    assert evidence["status"] == "PASS"
    assert evidence["actual_error_class"] == "OperationalError"


def test_sql_harness_can_assert_state_after_error_rollback():
    evidence = execute_sqlite(
        {
            "schema_version": 1,
            "id": "SQL-FND-0004",
            "document_id": "DBKB-FND-0026",
            "dialect": "sqlite",
            "environment": "sqlite-local",
            "setup": [
                "CREATE TABLE t (v INTEGER CHECK (v >= 0)); INSERT INTO t VALUES (10); "
                "BEGIN; UPDATE t SET v = 5;"
            ],
            "statement": "UPDATE t SET v = -1",
            "expectation": {
                "error_class": "IntegrityError",
                "message_contains": "CHECK constraint failed",
                "after_error": {"statement": "SELECT v FROM t", "rows": [[10]]},
            },
        }
    )
    assert evidence["status"] == "PASS"
    assert evidence["actual_rows"] == [[10]]


def test_sql_harness_marks_unavailable_engine_not_run(tmp_path: Path):
    example = {
        "schema_version": 1,
        "id": "SQL-FND-0003",
        "document_id": "DBKB-FND-0016",
        "dialect": "postgresql",
        "environment": "postgresql-container",
        "setup": [],
        "statement": "SELECT 1",
        "expectation": {"rows": [[1]]},
    }
    path = tmp_path / "SQL-FND-0003.yaml"
    path.write_text(yaml.safe_dump(example), encoding="utf-8")
    evidence = run_example(
        path,
        {
            "postgresql-container": {
                "available": False,
                "blocked_reason": "test environment unavailable",
            }
        },
    )
    assert evidence["status"] == "NOT_RUN"
    assert evidence["engine_version"] == "UNAVAILABLE"


def test_sql_harness_requires_opt_in_for_destructive_example():
    example = {
        "schema_version": 1,
        "id": "SQL-ISQL-0025",
        "document_id": "DBKB-ISQL-0025",
        "dialect": "sqlite",
        "environment": "sqlite-local",
        "setup": ["CREATE TABLE t (v INTEGER); INSERT INTO t VALUES (1);"],
        "statement": "SELECT v FROM t",
        "expectation": {"rows": [[1]]},
        "destructive": True,
    }
    assert execute_sqlite(example)["status"] == "BLOCKED"
    assert execute_sqlite(example, allow_destructive=True)["status"] == "PASS"


def test_docmost_dry_run_preserves_identity_and_never_deletes():
    local = {
        "DBKB-FND-0001": {
            "id": "DBKB-FND-0001",
            "path": "content/new.md",
            "content_sha256": "new",
        },
        "DBKB-FND-0002": {
            "id": "DBKB-FND-0002",
            "path": "content/two.md",
            "content_sha256": "same",
        },
    }
    remote = {
        "schema_version": 1,
        "pages": [
            {"id": "DBKB-FND-0001", "path": "content/old.md", "content_sha256": "old"},
            {"id": "DBKB-FND-0002", "path": "content/two.md", "content_sha256": "same"},
            {"id": "DBKB-FND-9999", "path": "content/orphan.md", "content_sha256": "x"},
        ],
    }
    plan = plan_sync(local, remote)
    assert [item["operation"] for item in plan["operations"]] == [
        "MOVE",
        "NO_CHANGE",
        "ARCHIVE_REVIEW_REQUIRED",
    ]
    assert "DELETE" not in json.dumps(plan)


def test_docmost_bundle_contains_only_eligible_markdown_and_identity_marker(tmp_path: Path):
    output = tmp_path / "bundle"
    manifest = build_bundle(Path(__file__).resolve().parents[1], output, "2026-01-01T00:00:00+00:00")
    assert manifest["document_count"] == 385
    assert manifest["zip"]["path"] == "docmost-import.zip"
    import zipfile

    with zipfile.ZipFile(output / "docmost-import.zip") as archive:
        assert len(archive.namelist()) == 385
        sample = archive.read(archive.namelist()[0]).decode("utf-8")
        assert sample.startswith("<!-- DBKB-ID: DBKB-")
        assert "schema_version:" not in sample
