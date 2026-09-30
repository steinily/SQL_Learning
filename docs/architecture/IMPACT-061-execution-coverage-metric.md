# Impact analysis — ADR-061

## Scope

The change affects only governance metrics and release-readiness calculation. Architecture v1.0, Manifest v1.0, document metadata, source records, Atlas fixtures and Docmost projection contracts remain unchanged.

## Affected components

| Component | Impact | Control |
|---|---|---|
| `scripts/kb_core.py` | Counts PASS execution evidence and preserves document-report count | Unit/integration tests and generated metrics |
| `PROJECT_STATUS.md` | Displays both coverage measures | Regenerated from metrics |
| `metrics/project-metrics.json` | Adds execution evidence numerator | JSON schema and validation |
| `scripts/sql_harness.py` | No semantic change; remains the evidence producer | Full harness run |
| `validation/execution/*.json` | More actual evidence records | Schema validation and checksums |
| Content/manifest | No change | Full repository validator |

## Risks

- A generated example could be low-value or duplicated. Mitigation: each case has a stable ID, setup, statement, expectation and actual evidence; coverage generation is deterministic and reviewed as a separate fixture set.
- Counting evidence without validating its declaration would permit orphan records. Mitigation: the metric joins PASS evidence to declared examples and ignores orphan evidence.
- Existing consumers may expect the old field. Mitigation: retain `passing_document_reports` and add the explicit `passing_execution_examples` field.

## Acceptance evidence

1. Repository validation has zero blocking findings.
2. Every counted execution case has a PASS evidence file produced by the harness.
3. The release gate reaches the frozen 1000-case target without modifying `manifest/v1.yaml`.
4. Existing pytest, Atlas, document audit and Docmost dry-run checks remain green.
