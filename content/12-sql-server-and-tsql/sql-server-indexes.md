---
schema_version: 1
id: DBKB-SS-0018
title: SQL Server Indexes
type: technology
primary_domain: sql-server
secondary_domains: [performance]
levels: [intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [sqlserver]
sql_dialects: [tsql]
scope: vendor-specific
prerequisites: [DBKB-SS-0008]
related: [DBKB-SS-0019, DBKB-SS-0020]
aliases: [SQL Server index]
search_keywords: [SQL Server index, access path, included columns]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-SS-0001]
source_ids: [SRC-000030]
acceptance_criteria: [Index célját, key/include column és write cost trade-offot adja]
---
# SQL Server Indexes

SQL Server index access pathot ad filter, join és ordering műveletekhez. Key column order, included columns, selectivity, storage és write maintenance workload evidence alapján tervezendő.

## Források
- [Microsoft Learn — Index architecture and design](https://learn.microsoft.com/sql/relational-databases/sql-server-index-design-guide)
