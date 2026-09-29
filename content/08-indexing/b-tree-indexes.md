---
schema_version: 1
id: DBKB-IDX-0003
title: B-tree Indexes
type: technology
primary_domain: indexing
secondary_domains: [postgresql]
levels: [intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-IDX-0001]
related: [DBKB-IDX-0005, DBKB-IDX-0020]
aliases: [btree]
search_keywords: [B-tree, range scan, equality index]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-IDX-0001]
source_ids: [SRC-000014]
acceptance_criteria: [B-tree equality/range és ordering use-case-et vendor scope-ban magyaráz]
---
# B-tree Indexes

A PostgreSQL B-tree általános célú access method equality és range feltételekhez, valamint megfelelő orderinghez. A column order és predicate alakja meghatározza, hogy használható-e.

## Források
- [PostgreSQL 18 — Index Types](https://www.postgresql.org/docs/18/indexes-types.html)
