---
schema_version: 1
id: DBKB-MODL-0024
title: Model Review Checklist
type: concept
primary_domain: data-modeling
secondary_domains: [governance, quality]
levels: [intermediate, advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [portable-sql, postgresql]
scope: cross-vendor
prerequisites: [DBKB-MODL-0017, DBKB-MODL-0019, DBKB-MODL-0022]
related: [DBKB-MODL-0023]
aliases: [schema design review]
search_keywords: [model review, checklist, grain, key, constraint, ownership]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-MODL-0003]
source_ids: [SRC-000009, SRC-000016]
acceptance_criteria: [Review kérdéseket completeness criteria-val ad, Evidence és owner mezőt követel]
---
# Model Review Checklist

Review kérdések: Mi egy row grainje? Mi a stable identity és alternate uniqueness? Mely relationship
cardinality/optionality bizonyított? Mely invariáns constraintként executable? Mi a `NULL` jelentése?

További kapuk: history/retention/timezone; tenant/security boundary; source of truth és owner; read/write
workload; migration/rollback; backfill és duplicate policy; observability; privacy és external exposure.

Minden „PASS” mellé evidence, reviewer, dátum és open risk tartozzon. „Schema compiles” nem teljes
model review.

## Források

- [PostgreSQL 18 — Constraints](https://www.postgresql.org/docs/18/ddl-constraints.html)
