---
schema_version: 1
id: DBKB-PERF-0005
title: Cost Model
type: concept
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
related: [DBKB-PERF-0013]
aliases: [planner cost]
search_keywords: [cost model, startup cost, total cost]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-PERF-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Estimated cost és elapsed time különbségét világosan elválasztja]
---
# Cost Model

Planner cost unit nem wall-clock milliseconds. A cost model I/O, CPU, row count és configuration assumptions alapján rangsorol terveket; validációhoz actual runtime és resource metrics is kell.

## Források
- [PostgreSQL 18 — Using EXPLAIN](https://www.postgresql.org/docs/18/using-explain.html)
