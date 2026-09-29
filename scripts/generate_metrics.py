from __future__ import annotations

import argparse
import json

try:
    from .kb_core import ROOT, collect_findings, generate_metrics, render_project_status
except ImportError:  # direct script execution
    from kb_core import ROOT, collect_findings, generate_metrics, render_project_status


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate deterministic project metrics")
    parser.add_argument("--generated-at", help="fixed ISO timestamp for reproducible fixtures")
    args = parser.parse_args()
    documents, findings = collect_findings(ROOT)
    metrics = generate_metrics(documents, findings, ROOT, args.generated_at)
    metrics_path = ROOT / "metrics" / "project-metrics.json"
    metrics_path.write_text(
        json.dumps(metrics, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    (ROOT / "PROJECT_STATUS.md").write_text(render_project_status(metrics), encoding="utf-8")
    print(f"generated {metrics_path.relative_to(ROOT)} and PROJECT_STATUS.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
