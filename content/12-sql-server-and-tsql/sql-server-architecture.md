---
schema_version: 1
id: DBKB-SS-0002
title: SQL Server Architecture
type: concept
primary_domain: sql-server
secondary_domains: [architecture]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [sqlserver]
sql_dialects: [tsql]
scope: vendor-specific
prerequisites: [DBKB-SS-0001]
related: [DBKB-SS-0003, DBKB-SS-0022]
aliases: [SQL Server Database Engine architecture]
search_keywords: [SQL Server architecture, Database Engine, instance, database]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-SS-0001]
source_ids: [SRC-000028, SRC-000030]
acceptance_criteria: [Instance, Database Engine, database és T-SQL layer kapcsolatát adja]
---
# SQL Server Architecture

SQL Server instance szolgáltatások és databases fölött futó Database Engine-t tartalmaz; T-SQL batch-eket parser, optimizer és execution engine kezel. Edition, platform és compatibility level behavior külön ellenőrzendő.

## Források
- [Microsoft Learn — SQL Server Database Engine](https://learn.microsoft.com/sql/relational-databases/database-engine/database-engine?view=sql-server-ver17)
