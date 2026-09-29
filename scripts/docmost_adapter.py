from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import Any

try:
    from .kb_core import ROOT, load_documents, load_json
except ImportError:  # direct script execution
    from kb_core import ROOT, load_documents, load_json


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def local_projection() -> dict[str, dict[str, Any]]:
    documents, findings = load_documents(ROOT)
    if findings:
        raise ValueError("cannot project documents with invalid front matter")
    return {
        document.metadata["id"]: {
            "id": document.metadata["id"],
            "title": document.metadata["title"],
            "path": str(document.path.relative_to(ROOT)),
            "content_sha256": digest(document.path),
        }
        for document in documents
        if document.metadata.get("publish") is True
        and document.metadata.get("maturity") in {"complete", "mature"}
        and document.metadata.get("verification") == "fully-verified"
    }


def plan_sync(
    local: dict[str, dict[str, Any]], remote_state: dict[str, Any]
) -> dict[str, Any]:
    remote = {page["id"]: page for page in remote_state.get("pages", [])}
    operations: list[dict[str, Any]] = []
    for doc_id, item in sorted(local.items()):
        prior = remote.get(doc_id)
        if prior is None:
            operations.append({"operation": "CREATE", "id": doc_id, "path": item["path"]})
        elif prior.get("path") != item["path"]:
            operations.append(
                {
                    "operation": "MOVE",
                    "id": doc_id,
                    "from": prior.get("path"),
                    "to": item["path"],
                }
            )
        elif prior.get("content_sha256") != item["content_sha256"]:
            operations.append({"operation": "UPDATE", "id": doc_id, "path": item["path"]})
        else:
            operations.append({"operation": "NO_CHANGE", "id": doc_id, "path": item["path"]})
    for doc_id in sorted(set(remote) - set(local)):
        operations.append(
            {
                "operation": "ARCHIVE_REVIEW_REQUIRED",
                "id": doc_id,
                "path": remote[doc_id].get("path"),
                "reason": "remote identity absent from eligible local projection; no automatic delete",
            }
        )
    counts = Counter(item["operation"] for item in operations)
    return {
        "schema_version": 1,
        "mode": "DRY_RUN",
        "operations": operations,
        "counts": dict(sorted(counts.items())),
        "live_publish": "BLOCKED_CREDENTIALS_OR_API_NOT_CONFIGURED",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Produce a non-mutating Docmost sync plan")
    parser.add_argument("--remote-state", type=Path, required=True)
    parser.add_argument("--output", type=Path, default=Path("generated/docmost-dry-run.json"))
    args = parser.parse_args()
    remote_path = args.remote_state if args.remote_state.is_absolute() else ROOT / args.remote_state
    output_path = args.output if args.output.is_absolute() else ROOT / args.output
    plan = plan_sync(local_projection(), load_json(remote_path))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(plan, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(plan["counts"], sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
