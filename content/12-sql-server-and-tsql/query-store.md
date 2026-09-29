---
schema_version: 1
id: DBKB-SS-0022
title: Query Store
type: technology
primary_domain: sql-server
secondary_domains: [observability]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [sqlserver]
sql_dialects: [tsql]
scope: vendor-specific
prerequisites: [DBKB-SS-0018]
related: [DBKB-SS-0023, DBKB-SS-0032]
aliases: [SQL Server Query Store]
search_keywords: [Query Store, query plan history, forced plan]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-SS-0001]
source_ids: [SRC-000030]
acceptance_criteria: [Query Store capture, plan history, regression és forcing caveat-et adja]
---
# Query Store

Query Store query, plan és runtime historyt per database tárol, így regressziók és plan changes vizsgálhatók. Capture overhead, retention, forced plan lifecycle és version support legyen explicit.

## Források
- [Microsoft Learn — Query Store](https://learn.microsoft.com/sql/relational-databases/performance/monitoring-performance-by-using-the-query-store)
