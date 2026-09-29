---
schema_version: 1
id: DBKB-PERF-0018
title: Sort and Hash Memory
type: concept
primary_domain: query-performance
secondary_domains: [operations]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-PERF-0004]
related: [DBKB-PERF-0010]
aliases: [work_mem, temp spill]
search_keywords: [sort memory, hash memory, disk spill, work_mem]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-PERF-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Memory spill és per-operation scope kockázatát dokumentálja]
---
# Sort and Hash Memory

Sort és hash operator memory spillt okozhat, ha a per-operation limit kevés; túl magas globális érték viszont concurrency alatt memory exhaustionhöz vezethet. Temp file evidence és workload concurrency alapján tuningolj.

## Források
- [PostgreSQL 18 — Resource Consumption](https://www.postgresql.org/docs/18/runtime-config-resource.html)
