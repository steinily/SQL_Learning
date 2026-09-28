# Codex Project Execution Contract

## Mission

Build the complete **Data & Database Engineering Knowledge Base** defined by this repository.

The repository is the specification. Do not replace its architecture with a simpler ad-hoc design.

## Read first, in order

1. `README.md`
2. `docs/architecture/ARCHITECTURE.md`
3. `docs/architecture/ADR.md`
4. `governance/POLICIES.md`
5. `governance/DEFINITION_OF_READY_DONE.md`
6. `manifest/v1.yaml`
7. `manifest/topic-catalog.yaml`
8. `manifest/m01-foundations.yaml`
9. `schemas/`
10. `qa/README.md`
11. `atlas/README.md`
12. `docmost/PUBLISHING_CONTRACT.md`

## Objective

Implement the repository infrastructure and then produce the complete V1 knowledge base. Work iteratively until all required V1 manifest items satisfy their Definition of Done.

Do not stop after scaffolding. Do not stop after M01. Continue module by module through V1 unless blocked by a genuine evidence, environment, licensing, access or human-review requirement.

## Non-negotiable rules

- GitHub repository content is canonical.
- Explanations are Hungarian; technical terms, code, identifiers and vendor terminology remain in original English.
- Never invent citations, versions, benchmark numbers, production incidents, execution results or vendor behavior.
- Model knowledge is not verification evidence.
- Prefer official primary documentation.
- A Writer cannot mark its own work fully verified.
- `execution-verified` requires actual execution.
- Unsupported claims use VERIFY_REQUIRED or another explicit uncertainty state.
- New topics do not silently expand V1 scope.
- Do not generate one Markdown file per keyword.
- Avoid duplicated theory in vendor documents; link to canonical concepts.
- Destructive examples require isolated opt-in tests.
- Generated files must be clearly separated from authored source.
- Never silently delete published/canonical content.
- Respect all schema versions and validation contracts.
- Do not weaken tests or gates merely to make CI green.

## Execution strategy

### Phase 0 — bootstrap tooling
Implement:
- repository directory structure
- schema validation
- front-matter parser
- manifest validator
- stable-ID uniqueness check
- internal-link checker
- prerequisite-cycle checker
- generated project metrics
- QA report format
- source/evidence records
- work-package handling
- test harness skeleton
- Docmost adapter interface/dry-run contract
- Atlas generator skeleton

### Phase 1 — pilot
Complete the M01 pilot documents listed in `manifest/m01-foundations.yaml`.
Run the entire research → write → validate → audit → metrics pipeline.

Fix architecture/tooling defects discovered by the pilot without weakening frozen architectural decisions. Architecture changes require an ADR.

### Phase 2 — M01
Complete and verify all required M01 documents.

### Phase 3 — V1
Continue in dependency order across M02–M36. Use bounded Work Packages, normally 5–15 documents or one coherent topic family.

### Phase 4 — integration
Complete Atlas fixtures, scenarios, executable tests, generated glossary/indexes, cross-dialect matrix, error KB, project metrics and Docmost publishing dry run.

### Phase 5 — V1 release candidate
Run all release gates and produce a release snapshot. V1 is not ready until the manifest-driven release Definition of Done passes.

## Research protocol

For each technical work package:
1. identify claims requiring evidence;
2. gather authoritative sources;
3. record technology/version/context;
4. flag disagreements;
5. create a research package;
6. only then write canonical content.

For current/version-sensitive vendor behavior, verify against current official documentation. Do not assume a version from memory.

## Content workflow

ARCHITECT → RESEARCHER → WRITER → VALIDATOR → AUDITOR → FINAL QA

These are logical roles. They may be implemented as separate passes rather than separate processes, but separation of duties must be preserved.

## Failure behavior

Stop the affected item, not the entire project, when possible.

Use:
- BLOCKED
- VERIFY_REQUIRED
- SOURCE_CONFLICT
- EXECUTION_NOT_TESTED
- VERSION_UNCONFIRMED
- HUMAN_REVIEW_REQUIRED

Continue independent work packages while blocked work remains visible in project status.

## Progress reporting

Update generated project metrics after each completed Work Package. Always report:
- baseline scope progress
- content progress
- verification progress
- executable validation coverage
- P0/P1/P2 progress
- open QA issues by severity
- blocked items
- knowledge debt
- release readiness

Never represent architecture completion as content completion.

## Completion condition

The project is complete only when the V1 release gates in repository governance pass. A large document count is not completion.
