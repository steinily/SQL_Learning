---
schema_version: 1
id: DBKB-SS-0008
title: T-SQL Data Types
type: reference
primary_domain: sql-server
secondary_domains: [tsql]
levels: [intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [sqlserver]
sql_dialects: [tsql]
scope: vendor-specific
prerequisites: [DBKB-SS-0007]
related: [DBKB-SS-0016]
aliases: [SQL Server data types]
search_keywords: [T-SQL data types, decimal, varchar, datetime2, conversion]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-SS-0001]
source_ids: [SRC-000030]
acceptance_criteria: [Numeric, character, temporal, binary és conversion trade-offokat adja]
---
# T-SQL Data Types

SQL Server data type választás precision, storage, collation, implicit conversion és indexability trade-off. `varchar`/`nvarchar`, `datetime2`, `decimal` és `uniqueidentifier` semantics explicit legyen; implicit cast plan regressiont okozhat.

## Források
- [Microsoft Learn — Data types (Transact-SQL)](https://learn.microsoft.com/sql/t-sql/data-types/data-types-transact-sql)
