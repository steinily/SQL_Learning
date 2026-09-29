---
schema_version: 1
id: DBKB-SS-0017
title: Table Variables
type: technology
primary_domain: sql-server
secondary_domains: [tsql]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [sqlserver]
sql_dialects: [tsql]
scope: vendor-specific
prerequisites: [DBKB-SS-0016]
related: [DBKB-SS-0015]
aliases: ["@table variable"]
search_keywords: [table variable, "@table", temp table comparison]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-SS-0001]
source_ids: [SRC-000030]
acceptance_criteria: [Table variable/temp table trade-offot cardinality és scope szerint adja]
---
# Table Variables

Table variable batch/procedure scope-ban deklarált table-like object. Kis, bounded datasetnél hasznos lehet, de cardinality/statistics és indexing behavior miatt nagy intermediate resultnál temp table vagy set-based rewrite lehet megfelelőbb.

## Források
- [Microsoft Learn — table (Transact-SQL)](https://learn.microsoft.com/sql/t-sql/data-types/table-transact-sql)
