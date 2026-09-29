---
schema_version: 1
id: DBKB-IDX-0010
title: Index Selectivity
type: concept
primary_domain: indexing
secondary_domains: [performance]
levels: [intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: cross-vendor
prerequisites: [DBKB-IDX-0002]
related: [DBKB-IDX-0011]
aliases: [predicate selectivity]
search_keywords: [selectivity, distinct values, planner estimate]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-IDX-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Selectivityt cardinality/statistics és plan döntéssel kapcsolja össze]
---
# Index Selectivity

Selectivity azt jelzi, hogy egy predicate a relation mekkora részét választja ki. Alacsony selectivitynél a sequential scan olcsóbb lehet; az index döntést ne intuition, hanem aktuális `EXPLAIN` evidence alapján hozd meg.

## Források
- [PostgreSQL 18 — Using EXPLAIN](https://www.postgresql.org/docs/18/using-explain.html)
