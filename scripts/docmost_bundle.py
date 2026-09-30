from __future__ import annotations

import argparse
import hashlib
import json
import re
import zipfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

try:
    from .kb_core import ROOT, load_documents
except ImportError:  # direct script execution
    from kb_core import ROOT, load_documents


FRONT_MATTER = re.compile(r"\A---\s*\n.*?\n---\s*\n?", re.DOTALL)
SAFE_NAME = re.compile(r"[^A-Za-z0-9._/-]+")


def eligible_documents(root: Path = ROOT) -> list[Any]:
    documents, findings = load_documents(root)
    if findings:
        raise ValueError("cannot build Docmost bundle with invalid document front matter")
    return sorted(
        (
            document
            for document in documents
            if document.metadata.get("publish") is True
            and document.metadata.get("maturity") in {"complete", "mature"}
            and document.metadata.get("verification") == "fully-verified"
        ),
        key=lambda document: str(document.path.relative_to(root)),
    )


def bundle_path(document: Any, root: Path) -> str:
    relative = document.path.relative_to(root / "content")
    parts = [SAFE_NAME.sub("-", part).strip("-") or "untitled" for part in relative.parts]
    return "/".join(parts)


def imported_body(document: Any) -> str:
    body = FRONT_MATTER.sub("", document.path.read_text(encoding="utf-8"), count=1)
    document_id = str(document.metadata["id"])
    marker = f"<!-- DBKB-ID: {document_id} -->\n"
    return marker + body.lstrip("\n")


def build_bundle(root: Path, output_dir: Path, generated_at: str | None = None) -> dict[str, Any]:
    documents = eligible_documents(root)
    output_dir.mkdir(parents=True, exist_ok=True)
    zip_path = output_dir / "docmost-import.zip"
    entries: list[dict[str, Any]] = []
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for document in documents:
            path = bundle_path(document, root)
            content = imported_body(document).encode("utf-8")
            info = zipfile.ZipInfo(path)
            info.date_time = (1980, 1, 1, 0, 0, 0)
            info.compress_type = zipfile.ZIP_DEFLATED
            archive.writestr(info, content)
            entries.append(
                {
                    "id": document.metadata["id"],
                    "title": document.metadata["title"],
                    "source_path": str(document.path.relative_to(root)),
                    "import_path": path,
                    "sha256": hashlib.sha256(content).hexdigest(),
                }
            )
    manifest = {
        "schema_version": 1,
        "bundle_type": "docmost-markdown-import",
        "source_of_truth": "github",
        "generated_at": generated_at or datetime.now(timezone.utc).isoformat(),
        "document_count": len(entries),
        "zip": {"path": zip_path.name, "sha256": hashlib.sha256(zip_path.read_bytes()).hexdigest()},
        "documents": entries,
        "notes": [
            "Front matter is removed before import; stable DBKB identity is retained in an HTML comment.",
            "This bundle is intended for Docmost UI Import pages → Import zip.",
            "No remote mutation or deletion is performed by this tool.",
        ],
    }
    (output_dir / "docmost-import-manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser(description="Build a Docmost Markdown import ZIP")
    parser.add_argument("--output-dir", type=Path, default=Path("generated/docmost-import"))
    parser.add_argument("--generated-at", help="fixed ISO timestamp for reproducible manifests")
    args = parser.parse_args()
    output_dir = args.output_dir if args.output_dir.is_absolute() else ROOT / args.output_dir
    manifest = build_bundle(ROOT, output_dir, args.generated_at)
    print(json.dumps({"documents": manifest["document_count"], "zip": manifest["zip"]["path"]}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
