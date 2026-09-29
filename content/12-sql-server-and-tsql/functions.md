---
schema_version: 1
id: DBKB-SS-0012
title: Functions
type: technology
primary_domain: sql-server
secondary_domains: [programming]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [sqlserver]
sql_dialects: [tsql]
scope: vendor-specific
prerequisites: [DBKB-SS-0011]
related: [DBKB-SS-0013]
aliases: [T-SQL user-defined function]
search_keywords: [SQL Server function, scalar UDF, table-valued function]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-SS-0001]
source_ids: [SRC-000030]
acceptance_criteria: [Scalar és table-valued function performance/security különbségét adja]
---
# Functions

SQL Server UDF scalar vagy table-valued resultot adhat. Function restrictions, determinism, schema binding és optimizer inlining version/compatibility-level függő; scalar UDF-t ne használj plan evidence nélkül nagy row seten.

## Források
- [Microsoft Learn — CREATE FUNCTION](https://learn.microsoft.com/sql/t-sql/statements/create-function-transact-sql)
