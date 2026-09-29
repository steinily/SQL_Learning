---
schema_version: 1
id: DBKB-SS-0014
title: Views
type: concept
primary_domain: sql-server
secondary_domains: [schema-design]
levels: [intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [sqlserver]
sql_dialects: [tsql]
scope: vendor-specific
prerequisites: [DBKB-SS-0007]
related: [DBKB-SS-0011]
aliases: [CREATE VIEW]
search_keywords: [SQL Server view, schemabinding, indexed view]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-SS-0001]
source_ids: [SRC-000030]
acceptance_criteria: [View, schemabinding és indexed view trade-offot adja]
---
# Views

View query abstractiont ad; `SCHEMABINDING` dependency contractot, indexed view pedig materialized maintenance costot hoz. Security ownership chain és optimizer behavior version/configuration szerint validálandó.

## Források
- [Microsoft Learn — CREATE VIEW](https://learn.microsoft.com/sql/t-sql/statements/create-view-transact-sql)
