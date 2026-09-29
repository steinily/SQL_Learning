---
schema_version: 1
id: DBKB-ASQL-0028
title: Modification Result Capture
type: concept
primary_domain: advanced-sql
secondary_domains: [data-integrity, integration]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql, sqlite]
sql_dialects: [postgresql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-SQL-0020, DBKB-SQL-0021]
related: [DBKB-ASQL-0024, DBKB-ASQL-0025]
aliases: [returning modified rows, output clause]
search_keywords: [returning, output, affected rows, audit]
risk: caution
version_sensitive: true
review_cycle: 6m
research_packages: [RP-ASQL-0003]
source_ids: [SRC-000043, SRC-000044]
acceptance_criteria:
  - Elkülöníti affected row countot és returned row payloadot.
  - PostgreSQL RETURNING scope-ot dokumentál.
  - SQLite fixture-ben readbackkel validál, nem vendor claimként.
---
# Modification Result Capture

Affected-row count csak mennyiségi ellenőrzés; audit vagy downstream integrationhez a módosított
identifier, old/new value és operation type is szükséges lehet. PostgreSQL `INSERT`, `UPDATE`,
`DELETE` és `MERGE` `RETURNING` clause-a ilyen resultot adhat, de privilege és dialect-specific.

Returned rows transaction outcome-ját a commit/rollback határozza meg. Consumer ne kezelje sikeresnek
a payloadot commit proof nélkül. Bulk operationnél result stream mérete, ordering és retry duplicate
policy is contract.

A `SQL-ASQL-0028` SQLite isolated DML után explicit readbacket ellenőriz. Ez nem állít PostgreSQL
`RETURNING` syntax executiont, amelyhez elérhető PostgreSQL adapter szükséges.

## Források

- [PostgreSQL 18 — INSERT](https://www.postgresql.org/docs/18/sql-insert.html)
- [PostgreSQL 18 — MERGE](https://www.postgresql.org/docs/18/sql-merge.html)
