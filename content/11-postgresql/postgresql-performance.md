---
schema_version: 1
id: DBKB-PG-0033
title: PostgreSQL Performance
type: playbook
primary_domain: postgresql
secondary_domains: [performance]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-PG-0025, DBKB-PERF-0023]
related: [DBKB-PG-0034]
aliases: [PostgreSQL tuning]
search_keywords: [PostgreSQL performance, autovacuum tuning, EXPLAIN]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-PG-0001]
source_ids: [SRC-000014]
acceptance_criteria: [EXPLAIN, statistics, vacuum, memory és I/O workflowet vendor scope-ban adja]
---
# PostgreSQL Performance

PostgreSQL tuning workflow: query plan/rows, statistics, indexes, vacuum, buffers/I/O, memory és concurrency signal együtt vizsgálandó. Configuration change csak baseline, staged test és rollback mellett kerüljön productionbe.

## Források
- [PostgreSQL 18 — Performance Tips](https://www.postgresql.org/docs/18/performance-tips.html)
