---
schema_version: 1
id: DBKB-ASQL-0027
title: Bulk Modification Patterns
type: concept
primary_domain: advanced-sql
secondary_domains: [operations, data-integrity]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql, sqlite]
sql_dialects: [portable-sql, postgresql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-SQL-0021, DBKB-FND-0024]
related: [DBKB-ASQL-0028]
aliases: [batch DML]
search_keywords: [bulk update, batch delete, chunking, affected rows]
risk: destructive
version_sensitive: true
review_cycle: 6m
research_packages: [RP-ASQL-0003]
source_ids: [SRC-000030, SRC-000031]
acceptance_criteria:
  - Preview/count/transaction/recovery workflow-t ad.
  - Tárgyalja a chunking és concurrent boundary kockázatát.
  - Isolated destructive fixture-t ad.
---
# Bulk Modification Patterns

Bulk `UPDATE` és `DELETE` előtt ugyanazzal a predicate-tel preview `SELECT`, expected count, backup és
recovery plan kell. Nagy table-nél chunking csökkentheti lock/runtime kockázatot, de a chunk boundary,
ordering és concurrent változás új correctness kérdés.

Explicit transaction, affected-row assertion, progress checkpoint és retry policy legyen. „Minden
sorhoz ugyanaz a transformation” esetén idempotenciát bizonyíts; partial retry ne duplázza vagy hagyja
ki a módosítást.

Foreign key cascade, trigger, audit row és index maintenance a target sorokon kívüli hatás. A
`SQL-ASQL-0027` isolated SQLite fixture-ben targeted update/delete végállapotot ellenőriz, destructive
opt-in mellett.

## Források

- [PostgreSQL 18 — Data Manipulation](https://www.postgresql.org/docs/18/dml.html)
- [Microsoft — Transact-SQL statements](https://learn.microsoft.com/sql/t-sql/statements/statements)
