from __future__ import annotations

import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

try:
    from .docmost_bundle import FRONT_MATTER, SAFE_NAME, eligible_documents, imported_body
    from .kb_core import ROOT
except ImportError:  # direct script execution
    from docmost_bundle import FRONT_MATTER, SAFE_NAME, eligible_documents, imported_body
    from kb_core import ROOT


def publication_path(document: Any, root: Path) -> Path:
    relative = document.path.relative_to(root / "content")
    parts = [SAFE_NAME.sub("-", part).strip("-") or "untitled" for part in relative.parts]
    return Path(*parts)


def build_publication(root: Path, output_dir: Path, generated_at: str | None = None) -> dict[str, Any]:
    documents = eligible_documents(root)
    output_dir.mkdir(parents=True, exist_ok=True)
    entries: list[dict[str, Any]] = []
    for document in documents:
        target = output_dir / publication_path(document, root)
        target.parent.mkdir(parents=True, exist_ok=True)
        content = imported_body(document)
        target.write_text(content, encoding="utf-8")
        entries.append(
            {
                "id": document.metadata["id"],
                "title": document.metadata["title"],
                "source_path": str(document.path.relative_to(root)),
                "publication_path": str(target.relative_to(output_dir)),
                "sha256": hashlib.sha256(content.encode("utf-8")).hexdigest(),
            }
        )
    entries.sort(key=lambda item: item["id"])
    readme = """# SQL Biblia\n\nThis repository is an automatically generated, read-only publication projection of `steinily/SQL_Glossary`.\n\nThe canonical source, metadata, research evidence and validation records remain in the source repository. Do not edit generated Markdown files here; changes will be overwritten by the publication workflow.\n\nEach page retains its stable `DBKB-ID` in an HTML comment.\n"""
    (output_dir / "README.md").write_text(readme, encoding="utf-8")
    manifest = {
        "schema_version": 1,
        "publication": "SQL_Biblia",
        "source_repository": "steinily/SQL_Glossary",
        "generated_at": generated_at or datetime.now(timezone.utc).isoformat(),
        "document_count": len(entries),
        "documents": entries,
    }
    (output_dir / "PUBLICATION_MANIFEST.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser(description="Build the SQL Biblia read-only projection")
    parser.add_argument("--output-dir", type=Path, default=Path("generated/sql-biblia"))
    parser.add_argument("--generated-at", help="fixed ISO timestamp for reproducible manifests")
    args = parser.parse_args()
    output_dir = args.output_dir if args.output_dir.is_absolute() else ROOT / args.output_dir
    manifest = build_publication(ROOT, output_dir, args.generated_at)
    print(json.dumps({"documents": manifest["document_count"], "output": str(output_dir)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
