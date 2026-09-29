---
schema_version: 1
id: DBKB-PG-0008
title: Data Types
type: reference
primary_domain: postgresql
secondary_domains: [schema-design]
levels: [intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-PG-0007]
related: [DBKB-PG-0009, DBKB-PG-0010]
aliases: [PostgreSQL type system]
search_keywords: [PostgreSQL data types, type casting, domains, enum]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-PG-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Built-in, user-defined, domain és cast fogalmakat scopeolja]
---
# Data Types

PostgreSQL type system built-in scalar, array, range, composite, enum, domain és user-defined typeokat támogat. Type választásnál storage, comparison, indexability, NULL semantics és migration compatibility együtt vizsgálandó.

## Források
- [PostgreSQL 18 — Data Types](https://www.postgresql.org/docs/18/datatype.html)
