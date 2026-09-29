---
schema_version: 1
id: DBKB-PERF-0002
title: EXPLAIN Fundamentals
type: concept
primary_domain: query-performance
secondary_domains: [postgresql]
levels: [intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-PERF-0001]
related: [DBKB-PERF-0003, DBKB-PERF-0004]
aliases: [query plan inspection]
search_keywords: [EXPLAIN, query plan, planner]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-PERF-0001]
source_ids: [SRC-000014]
acceptance_criteria: [EXPLAIN output alapfogalmait és caveatjeit leírja]
---
# EXPLAIN Fundamentals

Az `EXPLAIN` a planner által választott tervet mutatja, de önmagában nem futtatja a queryt. A node tree, estimated rows, cost és access method együtt értelmezendő.

## Források
- [PostgreSQL 18 — Using EXPLAIN](https://www.postgresql.org/docs/18/using-explain.html)
