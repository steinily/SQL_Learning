---
schema_version: 1
id: DBKB-SS-0021
title: Columnstore Indexes
type: technology
primary_domain: sql-server
secondary_domains: [analytics]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [sqlserver]
sql_dialects: [tsql]
scope: vendor-specific
prerequisites: [DBKB-SS-0018]
related: [DBKB-SS-0022]
aliases: [columnstore]
search_keywords: [columnstore index, batch mode, rowgroup]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-SS-0001]
source_ids: [SRC-000030]
acceptance_criteria: [Rowgroup, compression, batch mode és OLTP/OLAP trade-offot írja le]
---
# Columnstore Indexes

Columnstore index column-oriented compression és batch processing révén analytical scan/aggregate workloadot gyorsíthat. Rowgroup health, delta store, load pattern és mixed OLTP/OLAP impact version/edition szerint validálandó.

## Források
- [Microsoft Learn — Columnstore indexes](https://learn.microsoft.com/sql/relational-databases/indexes/columnstore-indexes-overview)
