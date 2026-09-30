# ADR-061 — Execution coverage counts evidence cases

Status: **PROPOSED FOR V1 RELEASE GATE**

Date: 2026-09-30

## Context

The frozen V1 manifest sets `release_targets.executable_tests_target_min` to 1000. The original metrics implementation counted passing document audit reports, although one document may contain zero, one or many executable examples. The baseline contains 918 documents, so that implementation could never reach a 1000 execution target and did not measure the named quantity.

## Decision

Release execution coverage is measured as the number of distinct execution evidence records with `status: PASS` for declared SQL examples. The metrics output retains document-level audit coverage separately. A document audit may report execution `PASS` when all of its declared examples pass; this is not used as the release target numerator.

## Consequences

- The metric matches the manifest wording and supports multiple examples per document.
- Every counted case must be declared in `examples/`, validated against the SQL example schema and actually run by `scripts/sql_harness.py`.
- Unsupported environments remain `BLOCKED` or `NOT_RUN` and never contribute to PASS coverage.
- Historical document reports remain valid evidence for document-level QA.
- Existing consumers of `execution_validation.passing_document_reports` remain supported; the release gate uses the new `passing_execution_examples` field.

## Alternatives rejected

- Lowering the frozen manifest target: would silently weaken the approved V1 baseline.
- Counting synthetic report files: would not be execution evidence.
- Marking unsupported vendor examples as PASS: prohibited by ADR-010, ADR-012 and ADR-045.

## Verification

The implementation is covered by the repository test suite, schema validation, and actual SQL harness execution. The impact analysis is recorded in `docs/architecture/IMPACT-061-execution-coverage-metric.md`.
