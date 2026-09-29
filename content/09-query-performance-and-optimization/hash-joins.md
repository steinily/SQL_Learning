---
schema_version: 1
id: DBKB-PERF-0010
title: Hash Joins
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
prerequisites: [DBKB-PERF-0004]
related: [DBKB-PERF-0018]
aliases: [hash join plan]
search_keywords: [hash join, hash table, work_mem]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-PERF-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Hash join build/probe és memory trade-offot bemutatja]
---
# Hash Joins

Hash join build oldalon hash table-t készít, probe oldalon ehhez keres. Memory pressure, spill és skew befolyásolhatja a tényleges runtime-ot; a tervet buffers és temp I/O adatokkal értékeld.

## Források
- [PostgreSQL 18 — Hash Join](https://www.postgresql.org/docs/18/using-explain.html)
