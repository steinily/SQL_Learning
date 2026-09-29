---
schema_version: 1
id: DBKB-IDX-0004
title: Hash Indexes
type: technology
primary_domain: indexing
secondary_domains: [postgresql]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-IDX-0001]
related: [DBKB-IDX-0003]
aliases: [hash access method]
search_keywords: [hash index, equality predicate]
risk: caution
version_sensitive: true
review_cycle: 6m
research_packages: [RP-IDX-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Hash index equality scopeját és korlátait megadja]
---
# Hash Indexes

A hash index equality összehasonlításokra szolgáló, vendor-specific access method. Nem általános replacement B-tree-re: range és ordering igényhez más index type szükséges.

## Források
- [PostgreSQL 18 — Index Types](https://www.postgresql.org/docs/18/indexes-types.html)
