---
schema_version: 1
id: DBKB-PG-0010
title: JSONB
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
related: [DBKB-PG-0014]
aliases: [jsonb data type]
search_keywords: [JSONB, json path, GIN JSONB]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-PG-0001]
source_ids: [SRC-000014]
acceptance_criteria: [JSON vs JSONB, operators, indexing és schema governance trade-offot ad]
---
# JSONB

`jsonb` parsed binary representationt tárol, amely query és indexing műveletekhez alkalmasabb lehet, mint text JSON. A flexible shape nem helyettesíti automatikusan relational constraintet; path, type és migration policy legyen explicit.

## Források
- [PostgreSQL 18 — JSON Types](https://www.postgresql.org/docs/18/datatype-json.html)
