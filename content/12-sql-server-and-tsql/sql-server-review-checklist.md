---
schema_version: 1
id: DBKB-SS-0040
title: SQL Server Review Checklist
type: playbook
primary_domain: sql-server
secondary_domains: [governance]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [sqlserver]
sql_dialects: [tsql]
scope: vendor-specific
prerequisites: [DBKB-SS-0037, DBKB-SS-0039]
related: [DBKB-SS-0038]
aliases: [SQL Server production review]
search_keywords: [SQL Server review, security review, HA review]
risk: production-critical
version_sensitive: false
review_cycle: 12m
research_packages: [RP-SS-0001]
source_ids: [SRC-000030]
acceptance_criteria: [Version, security, backup, HA, monitoring, performance és ownership review]
---
# SQL Server Review Checklist

Review legyen edition/version és compatibility inventory, login/role/TLS policy, backup/restore evidence, AG/failover drill, Query Store/Extended Events monitoring, performance baseline, upgrade/rollback és owner assignment.

## Források
- [Microsoft Learn — SQL Server security](https://learn.microsoft.com/sql/relational-databases/security/security-center-for-sql-server-database-engine-and-azure-sql-database)
