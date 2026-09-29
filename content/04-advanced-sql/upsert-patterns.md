---
schema_version: 1
id: DBKB-ASQL-0023
title: UPSERT Patterns
type: concept
primary_domain: advanced-sql
secondary_domains: [data-integrity, concurrency]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql, sqlite]
sql_dialects: [postgresql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-SQL-0020, DBKB-FND-0010]
related: [DBKB-ASQL-0024, DBKB-ASQL-0025]
aliases: [insert or update]
search_keywords: [upsert, conflict, unique, idempotency]
risk: caution
version_sensitive: true
review_cycle: 6m
research_packages: [RP-ASQL-0003]
source_ids: [SRC-000043]
acceptance_criteria:
  - Explicit conflict identityt és uniquenesset követel.
  - Elkülöníti a DO NOTHING és update outcome-ot.
  - SQLite-labelled executable mintát ad.
---
# UPSERT Patterns

Az UPSERT egy business key alapján insert vagy existing-row update döntést fejez ki. A conflict
identityt unique constraint/index biztosítsa; application-side „előbb SELECT, majd INSERT/UPDATE”
race conditiont hagy két concurrent writer között.

`DO NOTHING` idempotens retry boundary lehet, de nem adja vissza automatikusan a meglévő row-t.
`DO UPDATE` esetén a replacement, version predicate, timestamp és audit mező semanticset explicit
tervezd. Source batchben ugyanaz a conflict key többször ne jelenjen meg determinisztikusan.

Affected-row count, transaction isolation, trigger és returned-row behavior vendor-specific. A
`SQL-ASQL-0023` SQLite `ON CONFLICT DO UPDATE` statementet futtatja isolated fixture-en.

## Források

- [PostgreSQL 18 — INSERT](https://www.postgresql.org/docs/18/sql-insert.html)
