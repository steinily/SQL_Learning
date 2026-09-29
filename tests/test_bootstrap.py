from pathlib import Path
import json

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]


def test_all_json_schemas_are_valid():
    for path in (ROOT / "schemas").glob("*.schema.json"):
        Draft202012Validator.check_schema(json.loads(path.read_text(encoding="utf-8")))


def test_v1_has_all_modules():
    data = yaml.safe_load((ROOT / "manifest/v1.yaml").read_text(encoding="utf-8"))
    assert [m["id"] for m in data["modules"]] == [f"M{i:02d}" for i in range(1, 37)]


def test_m01_registry_has_35_unique_documents():
    data = yaml.safe_load((ROOT / "manifest/m01-foundations.yaml").read_text(encoding="utf-8"))
    ids = [row[0] for row in data["documents"]]
    assert len(ids) == 35
    assert len(ids) == len(set(ids))


def test_codex_contract_exists():
    assert (ROOT / "CODEX.md").is_file()
    assert "Do not stop after M01" in (ROOT / "CODEX.md").read_text(encoding="utf-8")


def test_all_work_packages_validate():
    schema = json.loads((ROOT / "schemas/work-package.schema.json").read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema)
    for path in (ROOT / "work-packages").glob("*.yaml"):
        validator.validate(yaml.safe_load(path.read_text(encoding="utf-8")))
