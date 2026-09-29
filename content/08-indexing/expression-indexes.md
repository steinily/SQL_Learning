---
schema_version: 1
id: DBKB-IDX-0008
title: Expression Indexes
type: technology
primary_domain: indexing
secondary_domains: [postgresql]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-IDX-0003]
related: [DBKB-IDX-0007]
aliases: [functional index]
search_keywords: [expression index, functional index]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-IDX-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Expression index és query expression egyezését leírja]
---
# Expression Indexes

Expression index számított értéket indexel, például normalizált vagy függvény-eredményt. A query expressionnek kompatibilisnek kell lennie az indexelt expressionnel; változó vagy nem immutable függvény külön kockázat.

## Források
- [PostgreSQL 18 — Indexes on Expressions](https://www.postgresql.org/docs/18/indexes-expressional.html)
