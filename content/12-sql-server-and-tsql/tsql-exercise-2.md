---
schema_version: 1
id: DBKB-SS-0036
title: T-SQL Exercise 2
type: exercise
primary_domain: sql-server
secondary_domains: [practice]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [sqlserver]
sql_dialects: [tsql]
scope: vendor-specific
prerequisites: [DBKB-SS-0025, DBKB-SS-0028]
related: [DBKB-SS-0038]
aliases: [SQL Server HA backup lab]
search_keywords: [T-SQL exercise, backup restore exercise, failover exercise]
risk: safe
version_sensitive: true
review_cycle: 12m
research_packages: [RP-SS-0001]
source_ids: [SRC-000030]
acceptance_criteria: [Recovery model, backup chain és failover drill tervezését gyakoroltatja]
---
# T-SQL Exercise 2

Készíts staging tesztmátrixot recovery modelhez, full/differential/log backup chainhez és Always On failover drillhez. Rögzíts RPO/RTO expectationt, restore/failover evidence-et, client reconnectet és rollbacket.

## Források
- [Microsoft Learn — Backup and restore](https://learn.microsoft.com/sql/relational-databases/backup-restore/backup-and-restore-of-sql-server-databases)
