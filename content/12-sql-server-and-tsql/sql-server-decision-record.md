---
schema_version: 1
id: DBKB-SS-0037
title: SQL Server Decision Record
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
prerequisites: [DBKB-SS-0033, DBKB-SS-0039]
related: [DBKB-PG-0037]
aliases: [SQL Server ADR]
search_keywords: [SQL Server decision record, HA ADR, T-SQL ADR]
risk: production-critical
version_sensitive: false
review_cycle: 12m
research_packages: [RP-SS-0001]
source_ids: [SRC-000030]
acceptance_criteria: [Edition/version, evidence, decision, impact, rollback és owner mezőket ad]
---
# SQL Server Decision Record

Rögzítsd SQL Server edition/versiont, compatibility levelt, topologyt, workloadot, evidence-et, chosen design/configurationt, security/performance/HA impactot, rollbacket, owner-t és review date-et.

## Források
- [Microsoft Learn — SQL Server documentation](https://learn.microsoft.com/sql/sql-server/)
