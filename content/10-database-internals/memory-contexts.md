---
schema_version: 1
id: DBKB-INT-0023
title: Memory Contexts
type: technology
primary_domain: database-internals
secondary_domains: [operations]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-INT-0007]
related: [DBKB-PERF-0018]
aliases: [memory context]
search_keywords: [memory context, backend memory, work_mem]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-INT-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Memory context és operator memory különbségét tisztázza]
---
# Memory Contexts

PostgreSQL memory context a backend és operator allocation életciklusát szervező belső mechanizmus. Nem azonos a `work_mem` globális pooljával; memory pressure diagnózisához process, operator, concurrency és OS evidence kell.

## Források
- [PostgreSQL 18 — Memory Contexts](https://www.postgresql.org/docs/18/memory-context.html)
