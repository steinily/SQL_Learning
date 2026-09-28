# Implementation Backlog

This backlog defines the initial implementation sequence. Codex should continue beyond it using the frozen V1 manifest.

## B00 — Repository tooling

Acceptance:
- parse YAML front matter
- validate document metadata with JSON Schema
- validate all JSON schemas themselves
- validate V1 and M01 manifests
- detect duplicate stable IDs
- check document ID references
- check internal Markdown links/anchors
- detect prerequisite cycles
- emit machine-readable QA results
- generate project metrics/status
- tests cover the validators

## B01 — Research/evidence infrastructure

Acceptance:
- source records validate
- research packages validate
- claim/evidence convention documented
- source conflicts and uncertainty are representable
- source freshness/version context can be recorded

## B02 — Atlas skeleton

Acceptance:
- version declaration
- deterministic seed strategy
- tiny dataset first
- organization/customer/product/order minimum slice
- dirty data remains separate
- fixture tests
- engine-neutral canonical model plus engine adapters where required

## B03 — SQL execution harness

Acceptance:
- example metadata identifies dialect/environment
- PostgreSQL and SQL Server are primary targets
- MySQL is secondary
- SQLite may be used for portable/local checks only when semantically valid
- expected result assertions
- expected-error assertions
- execution evidence is stored
- unsupported environments yield NOT_RUN/BLOCKED, never fake PASS

## B04 — M01 pilot

Use `WP-M01-001.yaml`.

Acceptance:
- six canonical documents
- authoritative research
- complete metadata
- QA reports
- links
- relevant executable examples
- metrics update
- no blocking findings

## B05 — Complete M01

All 35 M01 items satisfy domain DoD.

## B06 onward — V1 module execution

Generate file-level manifest entries before writing each module. Apply Architecture review and granular document rules. Execute modules in dependency-aware order, prioritizing P0.

Suggested broad order:
M02 → M03 → M05 → M06 → M07 → M08 → M09 → M10 → M11 → M12 → M13 → M16 → M17 → M18 → M19 → M20 → M22 → M25 → M27 → remaining P1 → P2 → M35 → M36 integration.

M04 may proceed after M03 prerequisites. Practical recipes/cases should be added continuously when their prerequisite concepts become verified, with final M35/M36 integration near release.

## B90 — Cross-cutting projections

- glossary
- indexes
- comparison matrix
- error KB indexes
- learning paths
- coverage map

## B95 — Docmost

Implement adapter/dry-run without making Docmost canonical. If credentials/API access are unavailable, complete the adapter interface/tests and mark live publish BLOCKED.

## B99 — V1 release candidate

Run full release gates, produce metrics snapshot, known limitations, knowledge/technical debt and release snapshot.
