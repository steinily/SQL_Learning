---
schema_version: 1
id: DBKB-PERF-0021
title: Predicate Pushdown
type: concept
primary_domain: query-performance
secondary_domains: [optimization]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: cross-vendor
prerequisites: [DBKB-PERF-0015, DBKB-PERF-0016]
related: [DBKB-PERF-0020]
aliases: [filter pushdown]
search_keywords: [predicate pushdown, filter pushdown, early filtering]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-PERF-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Pushdown benefitet és semantic boundaryt plan outputtal köti össze]
---
# Predicate Pushdown

Predicate pushdown a szűrést közelebb viszi az adatforráshoz, csökkentve az intermediate row countot. Outer join, volatile function és CTE materialization szemantikai boundaryt képezhet, ezért a rewrite plan és eredmény összevetésével bizonyítandó.

## Források
- [PostgreSQL 18 — Using EXPLAIN](https://www.postgresql.org/docs/18/using-explain.html)
