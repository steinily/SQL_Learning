from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / "schemas"


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def validate_schemas() -> list[str]:
    errors: list[str] = []
    for path in sorted(SCHEMAS.glob("*.schema.json")):
        try:
            schema = load_json(path)
            Draft202012Validator.check_schema(schema)
        except Exception as exc:
            errors.append(f"{path.relative_to(ROOT)}: invalid schema: {exc}")
    return errors


def validate_manifest_basics() -> list[str]:
    errors: list[str] = []
    v1 = yaml.safe_load((ROOT / "manifest/v1.yaml").read_text(encoding="utf-8"))
    modules = v1.get("modules", [])
    ids = [m.get("id") for m in modules]
    if len(ids) != len(set(ids)):
        errors.append("manifest/v1.yaml: duplicate module id")
    expected = {f"M{i:02d}" for i in range(1, 37)}
    missing = sorted(expected - set(ids))
    if missing:
        errors.append(f"manifest/v1.yaml: missing modules {missing}")

    m01 = yaml.safe_load((ROOT / "manifest/m01-foundations.yaml").read_text(encoding="utf-8"))
    doc_ids = [row[0] for row in m01.get("documents", [])]
    if len(doc_ids) != 35:
        errors.append(f"manifest/m01-foundations.yaml: expected 35 documents, got {len(doc_ids)}")
    if len(doc_ids) != len(set(doc_ids)):
        errors.append("manifest/m01-foundations.yaml: duplicate document id")
    pattern = re.compile(r"^DBKB-FND-\d{4}$")
    for doc_id in doc_ids:
        if not pattern.match(doc_id):
            errors.append(f"manifest/m01-foundations.yaml: invalid id {doc_id}")
    return errors


def main() -> int:
    errors = validate_schemas() + validate_manifest_basics()
    if errors:
        print("VALIDATION FAILED")
        for error in errors:
            print(f"- {error}")
        return 1
    print("VALIDATION PASSED")
    print("- JSON schemas are structurally valid")
    print("- V1 contains M01-M36 exactly")
    print("- M01 contains 35 unique DBKB-FND document IDs")
    return 0


if __name__ == "__main__":
    sys.exit(main())
