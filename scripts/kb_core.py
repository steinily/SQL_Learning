from __future__ import annotations

import hashlib
import json
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
from typing import Any, Iterable
from urllib.parse import unquote, urlsplit

import yaml
from jsonschema import Draft202012Validator, FormatChecker


ROOT = Path(__file__).resolve().parents[1]
DOCUMENT_ID = re.compile(r"^DBKB-[A-Z0-9]+-[0-9]{4}$")
FRONT_MATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*\n?", re.DOTALL)
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
HEADING = re.compile(r"^#{1,6}\s+(.+?)\s*#*\s*$", re.MULTILINE)


@dataclass(frozen=True)
class Document:
    path: Path
    metadata: dict[str, Any]
    body: str


@dataclass(frozen=True)
class Finding:
    severity: str
    code: str
    message: str
    evidence: str = ""

    def as_dict(self) -> dict[str, str]:
        result = {"severity": self.severity, "code": self.code, "message": self.message}
        if self.evidence:
            result["evidence"] = self.evidence
        return result


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def load_yaml(path: Path) -> Any:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def parse_front_matter(path: Path) -> Document:
    text = path.read_text(encoding="utf-8")
    match = FRONT_MATTER.match(text)
    if not match:
        raise ValueError("missing YAML front matter delimited by ---")
    metadata = yaml.safe_load(match.group(1))
    if not isinstance(metadata, dict):
        raise ValueError("front matter must be a YAML mapping")
    return Document(path=path, metadata=metadata, body=text[match.end() :])


def iter_content_paths(root: Path = ROOT) -> list[Path]:
    return sorted(
        path for path in (root / "content").rglob("*.md") if path.name.lower() != "readme.md"
    )


def load_documents(root: Path = ROOT) -> tuple[list[Document], list[Finding]]:
    documents: list[Document] = []
    findings: list[Finding] = []
    for path in iter_content_paths(root):
        try:
            documents.append(parse_front_matter(path))
        except (OSError, ValueError, yaml.YAMLError) as exc:
            findings.append(
                Finding("BLOCKER", "FRONT_MATTER_INVALID", str(exc), str(path.relative_to(root)))
            )
    return documents, findings


def schema_validator(name: str, root: Path = ROOT) -> Draft202012Validator:
    return Draft202012Validator(
        load_json(root / "schemas" / name), format_checker=FormatChecker()
    )


def validate_json_schemas(root: Path = ROOT) -> list[Finding]:
    findings: list[Finding] = []
    for path in sorted((root / "schemas").glob("*.schema.json")):
        try:
            Draft202012Validator.check_schema(load_json(path))
        except Exception as exc:
            findings.append(
                Finding("BLOCKER", "SCHEMA_INVALID", str(exc), str(path.relative_to(root)))
            )
    return findings


def _schema_findings(
    value: Any, validator: Draft202012Validator, relative_path: str, code: str
) -> list[Finding]:
    findings: list[Finding] = []
    for error in sorted(validator.iter_errors(value), key=lambda item: list(item.absolute_path)):
        location = ".".join(str(part) for part in error.absolute_path) or "$"
        findings.append(Finding("BLOCKER", code, f"{location}: {error.message}", relative_path))
    return findings


def validate_structured_records(root: Path = ROOT) -> list[Finding]:
    findings: list[Finding] = []
    locations = {
        "source.schema.json": root / "research" / "sources",
        "research-package.schema.json": root / "research" / "packages",
        "work-package.schema.json": root / "work-packages",
        "scenario.schema.json": root / "scenarios",
    }
    for schema_name, directory in locations.items():
        validator = schema_validator(schema_name, root)
        if not directory.exists():
            continue
        for path in sorted(directory.glob("*.yaml")):
            try:
                findings.extend(
                    _schema_findings(
                        load_yaml(path),
                        validator,
                        str(path.relative_to(root)),
                        "STRUCTURED_RECORD_INVALID",
                    )
                )
            except (OSError, yaml.YAMLError) as exc:
                findings.append(
                    Finding(
                        "BLOCKER",
                        "STRUCTURED_RECORD_PARSE_ERROR",
                        str(exc),
                        str(path.relative_to(root)),
                    )
                )
    example_validator = schema_validator("sql-example.schema.json", root)
    for path in sorted((root / "examples").rglob("SQL-*.yaml")):
        try:
            findings.extend(
                _schema_findings(
                    load_yaml(path),
                    example_validator,
                    str(path.relative_to(root)),
                    "SQL_EXAMPLE_INVALID",
                )
            )
        except (OSError, yaml.YAMLError) as exc:
            findings.append(
                Finding("BLOCKER", "SQL_EXAMPLE_PARSE_ERROR", str(exc), str(path.relative_to(root)))
            )
    evidence_validator = schema_validator("execution-evidence.schema.json", root)
    for path in sorted((root / "validation" / "execution").glob("*.json")):
        try:
            findings.extend(
                _schema_findings(
                    load_json(path),
                    evidence_validator,
                    str(path.relative_to(root)),
                    "EXECUTION_EVIDENCE_INVALID",
                )
            )
        except (OSError, json.JSONDecodeError) as exc:
            findings.append(
                Finding(
                    "BLOCKER", "EXECUTION_EVIDENCE_PARSE_ERROR", str(exc), str(path.relative_to(root))
                )
            )
    return findings


def document_registry(root: Path = ROOT) -> dict[str, dict[str, Any]]:
    registry: dict[str, dict[str, Any]] = {}
    for path in sorted((root / "manifest").glob("m??-*.yaml")):
        data = load_yaml(path) or {}
        for row in data.get("documents", []):
            if not isinstance(row, list) or len(row) < 3:
                continue
            registry[str(row[0])] = {
                "id": str(row[0]),
                "title": str(row[1]),
                "type": str(row[2]),
                "module": data.get("module"),
                "manifest": str(path.relative_to(root)),
            }
    return registry


def validate_manifests(root: Path = ROOT) -> list[Finding]:
    findings: list[Finding] = []
    try:
        v1 = load_yaml(root / "manifest" / "v1.yaml")
        modules = v1.get("modules", [])
        ids = [module.get("id") for module in modules]
        expected = [f"M{index:02d}" for index in range(1, 37)]
        if ids != expected:
            findings.append(
                Finding("BLOCKER", "V1_MODULE_SET", f"expected ordered {expected}, got {ids}")
            )
        if len(ids) != len(set(ids)):
            findings.append(Finding("BLOCKER", "DUPLICATE_MODULE_ID", "duplicate module ID"))
        catalog = load_yaml(root / "manifest" / "topic-catalog.yaml")
        if list((catalog.get("modules") or {}).keys()) != expected:
            findings.append(
                Finding(
                    "BLOCKER", "CATALOG_MODULE_SET", "topic catalog module order/set differs from v1"
                )
            )
    except (OSError, yaml.YAMLError, AttributeError) as exc:
        return [Finding("BLOCKER", "MANIFEST_PARSE_ERROR", str(exc))]

    seen: dict[str, str] = {}
    for path in sorted((root / "manifest").glob("m??-*.yaml")):
        data = load_yaml(path) or {}
        module = data.get("module")
        rows = data.get("documents") or []
        module_def = next((item for item in modules if item.get("id") == module), None)
        if module_def and len(rows) != module_def.get("target_docs"):
            findings.append(
                Finding(
                    "BLOCKER",
                    "MANIFEST_TARGET_MISMATCH",
                    f"{module}: expected {module_def.get('target_docs')} documents, got {len(rows)}",
                    str(path.relative_to(root)),
                )
            )
        for row in rows:
            if not isinstance(row, list) or len(row) != 3:
                findings.append(
                    Finding(
                        "BLOCKER",
                        "MANIFEST_ROW_INVALID",
                        "document entry must be [id, title, type]",
                        str(path.relative_to(root)),
                    )
                )
                continue
            doc_id, title, doc_type = row
            if not DOCUMENT_ID.fullmatch(str(doc_id)):
                findings.append(
                    Finding("BLOCKER", "DOCUMENT_ID_INVALID", str(doc_id), str(path.relative_to(root)))
                )
            if doc_id in seen:
                findings.append(
                    Finding(
                        "BLOCKER",
                        "DUPLICATE_MANIFEST_ID",
                        f"{doc_id} already registered in {seen[doc_id]}",
                        str(path.relative_to(root)),
                    )
                )
            seen[str(doc_id)] = str(path.relative_to(root))
            if not title or not doc_type:
                findings.append(
                    Finding("BLOCKER", "MANIFEST_ROW_EMPTY", str(row), str(path.relative_to(root)))
                )
    return findings


def github_anchor(title: str) -> str:
    value = re.sub(r"[`*_~]", "", title.strip().lower())
    value = re.sub(r"[^\w\- ]", "", value, flags=re.UNICODE)
    return re.sub(r"\s+", "-", value)


def anchors(text: str) -> set[str]:
    result: set[str] = set()
    counts: defaultdict[str, int] = defaultdict(int)
    for heading in HEADING.findall(text):
        base = github_anchor(heading)
        count = counts[base]
        result.add(base if count == 0 else f"{base}-{count}")
        counts[base] += 1
    return result


def _resolve_markdown_target(source: Path, raw_target: str, root: Path) -> tuple[Path, str] | None:
    target = raw_target.strip().strip("<>")
    parsed = urlsplit(target)
    if parsed.scheme or target.startswith("//") or target.startswith("mailto:"):
        return None
    path_part = unquote(parsed.path)
    if not path_part:
        return source, unquote(parsed.fragment)
    resolved = (
        root / path_part.lstrip("/")
        if path_part.startswith("/")
        else source.parent / PurePosixPath(path_part)
    )
    return resolved.resolve(), unquote(parsed.fragment)


def validate_documents(documents: list[Document], root: Path = ROOT) -> list[Finding]:
    findings: list[Finding] = []
    validator = schema_validator("document.schema.json", root)
    registry = document_registry(root)
    by_id: dict[str, list[Document]] = defaultdict(list)
    source_ids = {
        str((load_yaml(path) or {}).get("id"))
        for path in (root / "research" / "sources").glob("*.yaml")
    }
    research_ids = {
        str((load_yaml(path) or {}).get("id"))
        for path in (root / "research" / "packages").glob("*.yaml")
    }
    audit_reports: dict[str, dict[str, Any]] = {}
    for path in (root / "validation" / "documents").glob("*.json"):
        try:
            report = load_json(path)
            audit_reports[str(report.get("document_id"))] = report
        except (OSError, json.JSONDecodeError):
            continue
    for document in documents:
        relative = str(document.path.relative_to(root))
        findings.extend(
            _schema_findings(document.metadata, validator, relative, "DOCUMENT_METADATA_INVALID")
        )
        doc_id = document.metadata.get("id")
        if isinstance(doc_id, str):
            by_id[doc_id].append(document)
            entry = registry.get(doc_id)
            if not entry:
                findings.append(Finding("BLOCKER", "UNREGISTERED_DOCUMENT", doc_id, relative))
            else:
                if document.metadata.get("title") != entry["title"]:
                    findings.append(
                        Finding(
                            "MAJOR",
                            "MANIFEST_TITLE_MISMATCH",
                            f"expected {entry['title']!r}",
                            relative,
                        )
                    )
                if document.metadata.get("type") != entry["type"]:
                    findings.append(
                        Finding(
                            "MAJOR",
                            "MANIFEST_TYPE_MISMATCH",
                            f"expected {entry['type']!r}",
                            relative,
                        )
                    )
        for field in ("prerequisites", "related"):
            for reference in document.metadata.get(field, []):
                if reference not in registry:
                    findings.append(
                        Finding(
                            "BLOCKER",
                            "UNKNOWN_DOCUMENT_REFERENCE",
                            f"{field}: {reference}",
                            relative,
                        )
                    )
        for source_id in document.metadata.get("source_ids", []):
            if source_id not in source_ids:
                findings.append(
                    Finding("BLOCKER", "UNKNOWN_SOURCE_REFERENCE", source_id, relative)
                )
        for research_id in document.metadata.get("research_packages", []):
            if research_id not in research_ids:
                findings.append(
                    Finding("BLOCKER", "UNKNOWN_RESEARCH_REFERENCE", research_id, relative)
                )
        if document.metadata.get("verification") == "fully-verified":
            report = audit_reports.get(str(doc_id))
            if not report:
                findings.append(
                    Finding("BLOCKER", "FULL_VERIFICATION_WITHOUT_REPORT", str(doc_id), relative)
                )
            else:
                current_hash = hashlib.sha256(document.path.read_bytes()).hexdigest()
                if report.get("document_sha256") != current_hash:
                    findings.append(
                        Finding("BLOCKER", "STALE_VALIDATION_REPORT", str(doc_id), relative)
                    )
                required_pass = {
                    "content",
                    "sources",
                    "facts",
                    "dialects",
                    "metadata",
                    "links",
                    "duplication",
                    "contradictions",
                    "terminology",
                    "docmost_compatibility",
                }
                failed_dimensions = sorted(
                    name for name in required_pass if report.get("dimensions", {}).get(name) != "PASS"
                )
                if failed_dimensions or any(
                    item.get("severity") in {"BLOCKER", "CRITICAL", "MAJOR"}
                    for item in report.get("findings", [])
                ):
                    findings.append(
                        Finding(
                            "BLOCKER",
                            "FULL_VERIFICATION_GATE_FAILED",
                            ", ".join(failed_dimensions) or "blocking audit finding",
                            relative,
                        )
                    )
    for doc_id, instances in by_id.items():
        if len(instances) > 1:
            findings.append(
                Finding(
                    "BLOCKER",
                    "DUPLICATE_DOCUMENT_ID",
                    doc_id,
                    ", ".join(str(item.path.relative_to(root)) for item in instances),
                )
            )
    return findings


def validate_links(documents: list[Document], root: Path = ROOT) -> list[Finding]:
    findings: list[Finding] = []
    anchor_cache: dict[Path, set[str]] = {}
    for document in documents:
        relative = str(document.path.relative_to(root))
        full_text = document.path.read_text(encoding="utf-8")
        for raw_target in MARKDOWN_LINK.findall(document.body):
            resolved = _resolve_markdown_target(document.path, raw_target, root)
            if resolved is None:
                continue
            target_path, fragment = resolved
            try:
                target_path.relative_to(root.resolve())
            except ValueError:
                findings.append(Finding("MAJOR", "LINK_OUTSIDE_REPOSITORY", raw_target, relative))
                continue
            if not target_path.is_file():
                findings.append(Finding("MAJOR", "BROKEN_INTERNAL_LINK", raw_target, relative))
                continue
            if fragment and target_path.suffix.lower() == ".md":
                if target_path not in anchor_cache:
                    anchor_cache[target_path] = anchors(target_path.read_text(encoding="utf-8"))
                if fragment.lower() not in anchor_cache[target_path]:
                    findings.append(Finding("MAJOR", "BROKEN_INTERNAL_ANCHOR", raw_target, relative))
        if not full_text.endswith("\n"):
            findings.append(Finding("MINOR", "MISSING_FINAL_NEWLINE", "", relative))
    return findings


def prerequisite_cycles(documents: list[Document]) -> list[list[str]]:
    graph = {
        str(document.metadata.get("id")): list(document.metadata.get("prerequisites", []))
        for document in documents
        if document.metadata.get("id")
    }
    state: dict[str, int] = {}
    stack: list[str] = []
    cycles: list[list[str]] = []

    def visit(node: str) -> None:
        state[node] = 1
        stack.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in graph:
                continue
            if state.get(neighbor, 0) == 0:
                visit(neighbor)
            elif state.get(neighbor) == 1:
                cycle = stack[stack.index(neighbor) :] + [neighbor]
                if cycle not in cycles:
                    cycles.append(cycle)
        stack.pop()
        state[node] = 2

    for node in sorted(graph):
        if state.get(node, 0) == 0:
            visit(node)
    return cycles


def validate_graph(documents: list[Document]) -> list[Finding]:
    return [
        Finding("BLOCKER", "PREREQUISITE_CYCLE", " -> ".join(cycle))
        for cycle in prerequisite_cycles(documents)
    ]


def collect_findings(root: Path = ROOT) -> tuple[list[Document], list[Finding]]:
    documents, findings = load_documents(root)
    findings.extend(validate_json_schemas(root))
    findings.extend(validate_manifests(root))
    findings.extend(validate_structured_records(root))
    findings.extend(validate_documents(documents, root))
    findings.extend(validate_links(documents, root))
    findings.extend(validate_graph(documents))
    return documents, sorted(findings, key=lambda item: (item.severity, item.code, item.evidence))


def qa_report(findings: Iterable[Finding], executed_at: str | None = None) -> dict[str, Any]:
    finding_list = list(findings)
    passed = not any(item.severity in {"BLOCKER", "CRITICAL", "MAJOR"} for item in finding_list)
    encoded = json.dumps([item.as_dict() for item in finding_list], sort_keys=True).encode("utf-8")
    return {
        "schema_version": 1,
        "document_id": "REPOSITORY",
        "run_id": "repo-" + hashlib.sha256(encoded).hexdigest()[:12],
        "dimensions": {
            "schemas": "PASS" if not any(item.code == "SCHEMA_INVALID" for item in finding_list) else "FAIL",
            "manifests": "PASS" if not any("MANIFEST" in item.code or "MODULE_SET" in item.code for item in finding_list) else "FAIL",
            "metadata": "PASS" if not any("METADATA" in item.code or "FRONT_MATTER" in item.code for item in finding_list) else "FAIL",
            "links": "PASS" if not any("LINK" in item.code or "ANCHOR" in item.code for item in finding_list) else "FAIL",
            "knowledge_graph": "PASS" if not any("PREREQUISITE" in item.code for item in finding_list) else "FAIL",
            "release_gate": "PASS" if passed else "FAIL",
        },
        "findings": [item.as_dict() for item in finding_list],
        "executed_at": executed_at or datetime.now(timezone.utc).isoformat(),
    }


def validation_reports(root: Path = ROOT) -> list[dict[str, Any]]:
    reports: list[dict[str, Any]] = []
    validator = schema_validator("validation-report.schema.json", root)
    for path in sorted((root / "validation" / "documents").glob("*.json")):
        try:
            report = load_json(path)
        except (OSError, json.JSONDecodeError):
            continue
        if validator.is_valid(report):
            reports.append(report)
    return reports


def generate_metrics(
    documents: list[Document],
    findings: list[Finding],
    root: Path = ROOT,
    generated_at: str | None = None,
) -> dict[str, Any]:
    v1 = load_yaml(root / "manifest" / "v1.yaml")
    modules = v1["modules"]
    baseline_total = sum(int(module["target_docs"]) for module in modules)
    registry = document_registry(root)
    states = Counter(str(document.metadata.get("status", "unknown")) for document in documents)
    maturity = Counter(str(document.metadata.get("maturity", "unknown")) for document in documents)
    verification = Counter(
        str(document.metadata.get("verification", "unknown")) for document in documents
    )
    priorities = {module["id"]: module["priority"] for module in modules}
    module_by_id = {doc_id: data["module"] for doc_id, data in registry.items()}
    priority_totals = Counter(
        module["priority"] for module in modules for _ in range(module["target_docs"])
    )
    priority_authored = Counter(
        priorities.get(module_by_id.get(str(document.metadata.get("id")), ""), "UNKNOWN")
        for document in documents
    )
    severity = Counter(item.severity for item in findings)
    reports = validation_reports(root)
    fully_verified = sum(
        1 for document in documents if document.metadata.get("verification") == "fully-verified"
    )
    publishable = sum(
        1
        for document in documents
        if document.metadata.get("publish") is True
        and document.metadata.get("maturity") in {"complete", "mature"}
        and document.metadata.get("verification") == "fully-verified"
    )
    executable = sum(
        1
        for report in reports
        if report.get("dimensions", {}).get("execution") == "PASS"
    )
    blocking = sum(severity.get(level, 0) for level in ("BLOCKER", "CRITICAL", "MAJOR"))
    release_ready = (
        len(registry) == baseline_total
        and len(documents) == baseline_total
        and fully_verified == baseline_total
        and blocking == 0
        and executable >= int(v1["release_targets"]["executable_tests_target_min"])
    )
    return {
        "schema_version": 1,
        "generated_at": generated_at or datetime.now(timezone.utc).isoformat(),
        "baseline_scope": {
            "name": v1["baseline_scope"],
            "modules": len(modules),
            "target_documents": baseline_total,
            "registered_documents": len(registry),
            "registration_percent": round(len(registry) * 100 / baseline_total, 2),
            "priority_targets": dict(sorted(priority_totals.items())),
            "priority_authored": dict(sorted(priority_authored.items())),
        },
        "content": {
            "authored_documents": len(documents),
            "progress_percent": round(len(documents) * 100 / baseline_total, 2),
            "status": dict(sorted(states.items())),
            "maturity": dict(sorted(maturity.items())),
            "publishable_documents": publishable,
        },
        "verification": {
            "states": dict(sorted(verification.items())),
            "fully_verified": fully_verified,
            "progress_percent": round(fully_verified * 100 / baseline_total, 2),
        },
        "qa": {
            "findings_by_severity": {
                level: severity.get(level, 0)
                for level in ["BLOCKER", "CRITICAL", "MAJOR", "MINOR", "INFO"]
            },
            "blocking_findings": blocking,
        },
        "execution_validation": {
            "passing_document_reports": executable,
            "target_min": int(v1["release_targets"]["executable_tests_target_min"]),
        },
        "knowledge_graph": {
            "prerequisite_edges": sum(
                len(document.metadata.get("prerequisites", [])) for document in documents
            ),
            "cycles": len(prerequisite_cycles(documents)),
        },
        "source_health": {
            "research_packages": len(list((root / "research" / "packages").glob("*.yaml"))),
            "source_records": len(list((root / "research" / "sources").glob("*.yaml"))),
        },
        "knowledge_debt": {
            "unverified_documents": len(documents) - fully_verified,
            "unregistered_baseline_documents": baseline_total - len(registry),
        },
        "technical_debt": {
            "blocking_tooling_findings": blocking,
            "live_docmost_publish": "BLOCKED_CREDENTIALS_OR_API_NOT_CONFIGURED",
        },
        "release_ready": release_ready,
    }


def render_project_status(metrics: dict[str, Any]) -> str:
    baseline = metrics["baseline_scope"]
    content = metrics["content"]
    verification = metrics["verification"]
    qa = metrics["qa"]["findings_by_severity"]
    execution = metrics["execution_validation"]
    return f"""<!-- GENERATED: scripts/generate_metrics.py; DO NOT EDIT -->
# Project Status

Generated at: `{metrics['generated_at']}`

## Baseline scope

- Architecture: **v1.0 — FROZEN**
- Manifest: **v1.0 — FROZEN**
- Modules: **{baseline['modules']}**
- Target documents: **{baseline['target_documents']}**
- Registered documents: **{baseline['registered_documents']}** ({baseline['registration_percent']}%)

## Content and verification

- Authored documents: **{content['authored_documents']}** ({content['progress_percent']}%)
- Fully verified documents: **{verification['fully_verified']}** ({verification['progress_percent']}%)
- Publishable documents: **{content['publishable_documents']}**
- Execution-PASS document reports: **{execution['passing_document_reports']} / {execution['target_min']} minimum**

## QA

- BLOCKER: **{qa['BLOCKER']}**
- CRITICAL: **{qa['CRITICAL']}**
- MAJOR: **{qa['MAJOR']}**
- MINOR: **{qa['MINOR']}**
- INFO: **{qa['INFO']}**

## Debt and blockers

- Unverified authored documents: **{metrics['knowledge_debt']['unverified_documents']}**
- Unregistered baseline documents: **{metrics['knowledge_debt']['unregistered_baseline_documents']}**
- Live Docmost publish: **{metrics['technical_debt']['live_docmost_publish']}**

## Release readiness

**{'READY' if metrics['release_ready'] else 'NOT READY'}**

This result is produced by deterministic gates; it is not a project-health opinion.
"""
