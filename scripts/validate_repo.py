from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

try:
    from .kb_core import ROOT, collect_findings, qa_report
except ImportError:  # direct script execution
    from kb_core import ROOT, collect_findings, qa_report


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate the complete KB repository contract")
    parser.add_argument("--report", type=Path, help="write a schema-valid machine QA report")
    args = parser.parse_args()

    documents, findings = collect_findings(ROOT)
    report = qa_report(findings)
    if args.report:
        target = args.report if args.report.is_absolute() else ROOT / args.report
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    blocking = [item for item in findings if item.severity in {"BLOCKER", "CRITICAL", "MAJOR"}]
    print("VALIDATION PASSED" if not blocking else "VALIDATION FAILED")
    print(f"- content documents: {len(documents)}")
    print(f"- findings: {len(findings)} ({len(blocking)} blocking)")
    for finding in findings:
        suffix = f" [{finding.evidence}]" if finding.evidence else ""
        print(f"- {finding.severity} {finding.code}: {finding.message}{suffix}")
    return 1 if blocking else 0


if __name__ == "__main__":
    sys.exit(main())
