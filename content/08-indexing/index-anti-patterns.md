---
schema_version: 1
id: DBKB-IDX-0022
title: Index Anti-Patterns
type: troubleshooting
primary_domain: indexing
secondary_domains: [performance]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: cross-vendor
prerequisites: [DBKB-IDX-0010, DBKB-IDX-0012]
related: [DBKB-IDX-0023]
aliases: [over-indexing, redundant index]
search_keywords: [index anti-pattern, redundant index, over-indexing]
risk: production-critical
version_sensitive: false
review_cycle: 12m
research_packages: [RP-IDX-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Over-indexing, redundant index és untested index kockázatát felsorolja]
---
# Index Anti-Patterns

Gyakori anti-pattern a minden oszlopra létrehozott index, redundant prefix index, alacsony selectivity vak indexelése és plan nélkül végzett tuning. Minden indexhez owner, workload evidence és write/storage impact kell.

## Források
- [PostgreSQL 18 — Indexes](https://www.postgresql.org/docs/18/indexes.html)
