---
schema_version: 1
id: DBKB-PERF-0016
title: CTE Materialization
type: technology
primary_domain: query-performance
secondary_domains: [postgresql]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-PERF-0002]
related: [DBKB-PERF-0022]
aliases: [WITH materialization]
search_keywords: [CTE, materialized, NOT MATERIALIZED, inlining]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-PERF-0001]
source_ids: [SRC-000014]
acceptance_criteria: [CTE materialization version-sensitive behaviorét leírja]
---
# CTE Materialization

CTE materialization és inlining befolyásolja, hogy a planner pushdown és újrahasználat között hogyan optimalizál. PostgreSQL verzió és `MATERIALIZED`/`NOT MATERIALIZED` választás szerint különböző plan keletkezhet.

## Források
- [PostgreSQL 18 — WITH Queries](https://www.postgresql.org/docs/18/queries-with.html)
