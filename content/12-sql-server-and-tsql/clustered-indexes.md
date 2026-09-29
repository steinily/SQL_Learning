---
schema_version: 1
id: DBKB-SS-0019
title: Clustered Indexes
type: technology
primary_domain: sql-server
secondary_domains: [storage]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [sqlserver]
sql_dialects: [tsql]
scope: vendor-specific
prerequisites: [DBKB-SS-0018]
related: [DBKB-SS-0020]
aliases: [clustered index]
search_keywords: [clustered index, leaf level, heap]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-SS-0001]
source_ids: [SRC-000030]
acceptance_criteria: [Clustered leaf storage és one-per-table constraintet adja]
---
# Clustered Indexes

SQL Server clustered index leaf levelén a table data sorai rendezett index structure-ben vannak; egy table-nek legfeljebb egy clustered indexe lehet. Key design, fragmentation, page splits és range workload együtt vizsgálandó.

## Források
- [Microsoft Learn — Clustered and nonclustered indexes](https://learn.microsoft.com/sql/relational-databases/indexes/clustered-and-nonclustered-indexes-described)
