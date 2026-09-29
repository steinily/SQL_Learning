---
schema_version: 1
id: DBKB-SS-0020
title: Nonclustered Indexes
type: technology
primary_domain: sql-server
secondary_domains: [performance]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [sqlserver]
sql_dialects: [tsql]
scope: vendor-specific
prerequisites: [DBKB-SS-0018]
related: [DBKB-SS-0019, DBKB-SS-0021]
aliases: [nonclustered index, included column]
search_keywords: [nonclustered index, INCLUDE, covering index]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-SS-0001]
source_ids: [SRC-000030]
acceptance_criteria: [Key/include column, lookup és covering trade-offot adja]
---
# Nonclustered Indexes

Nonclustered index külön index structure, amely key columns és opcionális included columns alapján lookupot végezhet a clustered/heap data felé. Covering csökkentheti lookupot, de storage és write costot növel.

## Források
- [Microsoft Learn — Nonclustered indexes](https://learn.microsoft.com/sql/relational-databases/indexes/clustered-and-nonclustered-indexes-described)
