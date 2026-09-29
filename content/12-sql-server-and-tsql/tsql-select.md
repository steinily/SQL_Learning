---
schema_version: 1
id: DBKB-SS-0007
title: T-SQL SELECT
type: concept
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
prerequisites: [DBKB-SS-0006]
related: [DBKB-SS-0015]
aliases: [SELECT Transact-SQL]
search_keywords: [T-SQL SELECT, TOP, OFFSET FETCH, logical processing]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-SS-0001]
source_ids: [SRC-000028]
acceptance_criteria: [SELECT, FROM, WHERE, GROUP BY, ORDER BY és TOP scopeját adja]
---
# T-SQL SELECT

T-SQL `SELECT` projectiont, sourceot, filtert, groupingot és orderinget kombinál. `TOP`, `OFFSET/FETCH`, `APPLY` és logical processing order SQL Server-specific behaviorrel bír; deterministic ORDER BY nélkül pagination nem garantált.

## Források
- [Microsoft Learn — SELECT (Transact-SQL)](https://learn.microsoft.com/sql/t-sql/queries/select-transact-sql/)
