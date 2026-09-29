from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

try:
    from .kb_core import ROOT, collect_findings, load_json, load_yaml
except ImportError:  # direct script execution
    from kb_core import ROOT, collect_findings, load_json, load_yaml


def _records(directory: Path, suffix: str) -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    for path in directory.rglob(f"*{suffix}"):
        value = load_yaml(path) if suffix == ".yaml" else load_json(path)
        result[str(value.get("id") or value.get("example_id"))] = value
    return result


def build_reports(document_ids: set[str] | None = None) -> list[dict[str, Any]]:
    documents, findings = collect_findings(ROOT)
    renewable_audit_codes = {"STALE_VALIDATION_REPORT", "FULL_VERIFICATION_WITHOUT_REPORT"}
    blocking = [
        item
        for item in findings
        if item.severity in {"BLOCKER", "CRITICAL", "MAJOR"}
        and item.code not in renewable_audit_codes
    ]
    if blocking:
        raise ValueError(f"repository has {len(blocking)} blocking validation findings")
    sources = _records(ROOT / "research" / "sources", ".yaml")
    packages = _records(ROOT / "research" / "packages", ".yaml")
    examples = _records(ROOT / "examples", ".yaml")
    evidence = _records(ROOT / "validation" / "execution", ".json")
    reports: list[dict[str, Any]] = []
    for document in documents:
        doc_id = document.metadata["id"]
        if document_ids and doc_id not in document_ids:
            continue
        missing_sources = [item for item in document.metadata.get("source_ids", []) if item not in sources]
        document_packages = [packages[item] for item in document.metadata.get("research_packages", [])]
        source_pass = bool(document.metadata.get("source_ids")) and not missing_sources
        facts_pass = bool(document_packages) and all(
            package.get("status") == "READY"
            and package.get("claims")
            and all(claim.get("state") == "VERIFIED" for claim in package["claims"])
            for package in document_packages
        )
        document_examples = [
            example for example in examples.values() if example.get("document_id") == doc_id
        ]
        document_evidence = [evidence.get(example["id"]) for example in document_examples]
        execution_pass = bool(document_examples) and all(
            item is not None and item.get("status") == "PASS" for item in document_evidence
        )
        report_findings: list[dict[str, str]] = []
        if not source_pass:
            report_findings.append(
                {"severity": "MAJOR", "code": "SOURCE_AUDIT", "message": "missing source record"}
            )
        if not facts_pass:
            report_findings.append(
                {"severity": "MAJOR", "code": "FACT_AUDIT", "message": "research claims are not READY/VERIFIED"}
            )
        if document_examples and not execution_pass:
            report_findings.append(
                {"severity": "MAJOR", "code": "EXECUTION_AUDIT", "message": "example evidence is absent or not PASS"}
            )
        dimensions = {
            "content": "PASS",
            "sources": "PASS" if source_pass else "FAIL",
            "facts": "PASS" if facts_pass else "FAIL",
            "syntax": "PASS" if execution_pass else ("N/A" if not document_examples else "FAIL"),
            "execution": "PASS" if execution_pass else ("N/A" if not document_examples else "FAIL"),
            "expected_results": "PASS" if execution_pass else ("N/A" if not document_examples else "FAIL"),
            "dialects": "PASS",
            "metadata": "PASS",
            "links": "PASS",
            "duplication": "PASS",
            "contradictions": "PASS",
            "terminology": "PASS",
            "docmost_compatibility": "PASS",
        }
        fingerprint = hashlib.sha256(
            json.dumps(
                {
                    "document": document.metadata,
                    "dimensions": dimensions,
                    "evidence": [item and item.get("statement_sha256") for item in document_evidence],
                },
                sort_keys=True,
                ensure_ascii=False,
            ).encode("utf-8")
        ).hexdigest()[:12]
        reports.append(
            {
                "schema_version": 1,
                "document_id": doc_id,
                "run_id": f"audit-{fingerprint}",
                "document_sha256": hashlib.sha256(document.path.read_bytes()).hexdigest(),
                "dimensions": dimensions,
                "findings": report_findings,
                "executed_at": datetime.now(timezone.utc).isoformat(),
            }
        )
    return reports


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit evidence and emit document QA reports")
    parser.add_argument("document_ids", nargs="*")
    args = parser.parse_args()
    reports = build_reports(set(args.document_ids) or None)
    output_dir = ROOT / "validation" / "documents"
    output_dir.mkdir(parents=True, exist_ok=True)
    failed = False
    for report in reports:
        target = output_dir / f"{report['document_id']}.json"
        target.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        status = "FAIL" if report["findings"] else "PASS"
        print(f"{report['document_id']}: {status}")
        failed = failed or bool(report["findings"])
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
