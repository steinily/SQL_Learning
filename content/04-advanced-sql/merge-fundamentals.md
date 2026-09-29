---
schema_version: 1
id: DBKB-ASQL-0025
title: MERGE Fundamentals
type: concept
primary_domain: advanced-sql
secondary_domains: [data-integrity]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-ASQL-0023, DBKB-ISQL-0020]
related: [DBKB-ASQL-0026]
aliases: [merge statement]
search_keywords: [merge, matched, not matched, source target]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-ASQL-0003]
source_ids: [SRC-000044]
acceptance_criteria:
  - Elkülöníti source és target relationt.
  - Bemutatja a matched/not matched branch-eket.
  - PostgreSQL 18 source scope-ot rögzít.
---
# MERGE Fundamentals

`MERGE` source és target sorokat joinol, majd branch condition alapján `INSERT`, `UPDATE` vagy
`DELETE` actiont hajt végre. A source/target match predicate és branch order a correctness alapja.

Source batch uniqueness nélkül ugyanazt a target row-t több branch candidate érintheti vagy cardinality
error keletkezhet. A target unique constraint, expected affected-row count és postcondition legyen
explicit.

PostgreSQL 18 `MERGE` egy statementben keverheti a három DML actiont, és `RETURNING`-gel resultot
adhat. Más vendorok syntaxa, branch rules, error és concurrency behavior-je nem vezethető le ebből.

Local PostgreSQL unavailable, ezért ez source-verified, nem execution-verified.

## Források

- [PostgreSQL 18 — MERGE](https://www.postgresql.org/docs/18/sql-merge.html)
