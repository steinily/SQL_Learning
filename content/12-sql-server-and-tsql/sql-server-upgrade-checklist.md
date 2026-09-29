---
schema_version: 1
id: DBKB-SS-0039
title: SQL Server Upgrade Checklist
type: playbook
primary_domain: sql-server
secondary_domains: [operations]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [sqlserver]
sql_dialects: [tsql]
scope: vendor-specific
prerequisites: [DBKB-SS-0003, DBKB-SS-0028]
related: [DBKB-SS-0040]
aliases: [SQL Server upgrade runbook]
search_keywords: [SQL Server upgrade, compatibility level, migration checklist]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-SS-0001]
source_ids: [SRC-000030]
acceptance_criteria: [Precheck, compatibility, rehearsal, cutover, validation és rollback lépéseket ad]
---
# SQL Server Upgrade Checklist

Precheck edition/version, compatibility level, deprecated features, drivers, Agent jobs, SSIS/linked servers, backup/restore és HA. Rehearsal után cutover, smoke/performance validation, Query Store comparison és rollback window következik.

## Források
- [Microsoft Learn — Upgrade SQL Server](https://learn.microsoft.com/sql/database-engine/install-windows/upgrade-sql-server)
