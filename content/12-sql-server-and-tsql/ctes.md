---
schema_version: 1
id: DBKB-SS-0015
title: CTEs
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
prerequisites: [DBKB-SS-0007]
related: [DBKB-SS-0016]
aliases: [WITH common table expression]
search_keywords: [T-SQL CTE, recursive CTE, WITH clause]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-SS-0001]
source_ids: [SRC-000030]
acceptance_criteria: [Nonrecursive/recursive CTE scopeját és materialization caveatjét adja]
---
# CTEs

Common table expression query-scope named result expression, amely olvashatóságot és recursive traversal-t adhat. CTE nem automatikusan materialized temp object; optimizer behavior és repeated reference cost plan alapján értékelendő.

## Források
- [Microsoft Learn — WITH common_table_expression](https://learn.microsoft.com/sql/t-sql/queries/with-common-table-expression-transact-sql)
