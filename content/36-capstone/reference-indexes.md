---
schema_version: 1
id: DBKB-CAP-0053
title: Reference Indexes
type: reference
primary_domain: capstone
secondary_domains: [performance, sql]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql, sqlite]
sql_dialects: [postgresql, tsql, mysql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-CAP-0052]
related: [DBKB-IDX-0001]
aliases: [index checklist]
search_keywords: [index reference, selectivity, composite order, bloat, rebuild]
risk: production-critical
version_sensitive: false
review_cycle: 12m
research_packages: [RP-CAPSTONE-0001]
source_ids: [SRC-000001]
acceptance_criteria: [Index candidate, plan, write cost, maintenance, rollback and evidence checklist is provided]
---
# Reference Indexes

Review: query shape/predicate/order; selectivity/cardinality; composite order; write/storage cost; duplicate/unused index; build lock; statistics; bloat/fragmentation; explain before/after; rollback.

Index creation or removal is not automatically safe. Validate correctness, p95 latency, write impact and workload-specific resource profile with actual execution.

## Forrás
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
