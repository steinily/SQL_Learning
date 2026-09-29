---
schema_version: 1
id: DBKB-IDX-0019
title: Foreign Key Indexing
type: concept
primary_domain: indexing
secondary_domains: [data-modeling]
levels: [intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: cross-vendor
prerequisites: [DBKB-IDX-0003]
related: [DBKB-IDX-0021]
aliases: [referential index]
search_keywords: [foreign key index, parent delete, referential integrity]
risk: production-critical
version_sensitive: false
review_cycle: 12m
research_packages: [RP-IDX-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Foreign key child-side indexing rationale és workload caveat]
---
# Foreign Key Indexing

Foreign key constraint nem minden engine-ben hoz létre automatikus child-side indexet. Delete/update és join workloadnál a referencing column indexe csökkentheti scan és locking költségét; ezt execution plan és write cost alapján mérd.

## Források
- [PostgreSQL 18 — Foreign Keys](https://www.postgresql.org/docs/18/ddl-constraints.html#DDL-CONSTRAINTS-FK)
