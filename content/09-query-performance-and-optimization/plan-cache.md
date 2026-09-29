---
schema_version: 1
id: DBKB-PERF-0027
title: Plan Cache
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
prerequisites: [DBKB-PERF-0014]
related: [DBKB-PERF-0028]
aliases: [cached execution plan]
search_keywords: [plan cache, prepared plan, generic plan]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-PERF-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Plan reuse, invalidation és parameter sensitivity kapcsolatát leírja]
---
# Plan Cache

Plan reuse csökkentheti a planning overheadet, de stale vagy parameter distributionre rosszul illeszkedő tervet is újrahasználhat. PostgreSQL-ben prepared statement behavior és statistics változás befolyásolja a custom/generic tervet.

## Források
- [PostgreSQL 18 — PREPARE](https://www.postgresql.org/docs/18/sql-prepare.html)
