---
schema_version: 1
id: DBKB-IDX-0005
title: Composite Indexes
type: concept
primary_domain: indexing
secondary_domains: [performance]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-IDX-0003]
related: [DBKB-IDX-0006, DBKB-IDX-0021]
aliases: [multicolumn index]
search_keywords: [composite index, multicolumn index, leftmost column]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-IDX-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Column order és predicate prefix szabályát leírja]
---
# Composite Indexes

Multicolumn indexnél a column order nem felcserélhető részlet: a leading columnokra illeszkedő predicate gyakran fontosabb, mint a puszta column count. Tervezd a valós query workload és `EXPLAIN` alapján.

## Források
- [PostgreSQL 18 — Multicolumn Indexes](https://www.postgresql.org/docs/18/indexes-multicolumn.html)
