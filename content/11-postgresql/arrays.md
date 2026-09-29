---
schema_version: 1
id: DBKB-PG-0011
title: Arrays
type: technology
primary_domain: postgresql
secondary_domains: [data-modeling]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-PG-0008]
related: [DBKB-PG-0012]
aliases: [PostgreSQL array type]
search_keywords: [PostgreSQL array, array operators, unnest]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-PG-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Array indexing, unnest és normalization trade-offot magyaráz]
---
# Arrays

PostgreSQL array collection-typeként tárolható, de element ordering, NULL és cardinality semantics explicit legyen. `unnest` és array operators hasznosak lehetnek, azonban relational join/constraint igényt ne rejts el indokolatlanul array mögé.

## Források
- [PostgreSQL 18 — Arrays](https://www.postgresql.org/docs/18/arrays.html)
