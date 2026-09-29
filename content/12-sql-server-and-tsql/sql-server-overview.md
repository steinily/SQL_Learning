---
schema_version: 1
id: DBKB-SS-0001
title: SQL Server Overview
type: overview
primary_domain: sql-server
secondary_domains: [microsoft]
levels: [intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [sqlserver]
sql_dialects: [tsql]
scope: vendor-specific
prerequisites: [DBKB-PG-0040]
related: [DBKB-SS-0002, DBKB-SS-0006]
aliases: [Microsoft SQL Server]
search_keywords: [SQL Server, Microsoft database, T-SQL]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-SS-0001]
source_ids: [SRC-000028, SRC-000030]
acceptance_criteria: [SQL Server és T-SQL scopeját, version caveatjét összefoglalja]
---
# SQL Server Overview

Microsoft SQL Server relational database platform, amely T-SQL nyelvet és engine-specific security, HA, backup és performance képességeket biztosít. Minden feature claimhez target edition/version applies-to ellenőrzés kell.

## Források
- [Microsoft Learn — SQL Server documentation](https://learn.microsoft.com/sql/sql-server/)
