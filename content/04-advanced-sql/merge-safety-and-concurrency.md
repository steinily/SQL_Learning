---
schema_version: 1
id: DBKB-ASQL-0026
title: MERGE Safety and Concurrency
type: concept
primary_domain: advanced-sql
secondary_domains: [concurrency, operations]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-ASQL-0025, DBKB-FND-0024]
related: [DBKB-ASQL-0023, DBKB-SQL-0021]
aliases: [safe merge]
search_keywords: [merge concurrency, race, source uniqueness, retry]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-ASQL-0003]
source_ids: [SRC-000044]
acceptance_criteria:
  - Source uniqueness és target identity ellenőrzést ír elő.
  - Transaction/isolation/retry kérdéseket kezeli.
  - Production execution állítást nem talál ki.
---
# MERGE Safety and Concurrency

`MERGE` syntax önmagában nem bizonyít idempotenciát vagy race-free operationt. A source batchnek a
match key-en unique-nek kell lennie, a targetnek megfelelő unique constraint kell, és a concurrent
writer interactiont isolation/locking policyval kell megtervezni.

Biztonságos rollout: source profiling; dry-run match counts; insert/update/delete counts; explicit
transaction; constraint/error monitoring; postcondition és retry policy. Részleges failure esetén
rollback és replay semantics legyen dokumentált.

A branch condition `NULL`-ja nem `TRUE`; unmatched és ineligible sorok külön kategóriák. Trigger,
foreign key, audit és `RETURNING` output miatt a row count önmagában nem teljes bizonyíték.

PostgreSQL 18 source alapján készült; local runtime hiányában execution dimenziója `N/A`.

## Források

- [PostgreSQL 18 — MERGE](https://www.postgresql.org/docs/18/sql-merge.html)
