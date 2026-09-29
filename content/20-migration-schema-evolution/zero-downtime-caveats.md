---
schema_version: 1
id: DBKB-MIG-0016
title: Zero Downtime Caveats
type: troubleshooting
primary_domain: migration
secondary_domains: [reliability]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-MIG-0015]
related: []
aliases: [online migration caveats]
search_keywords: [zero downtime, metadata lock, brief outage, cutover]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-MIG-0001]
source_ids: [SRC-000060, SRC-000061, SRC-000062]
acceptance_criteria: [Downtime sources, cutover windows and false guarantees are explained]
---
# Zero Downtime Caveats

Zero downtime claimet megtörheti metadata lock, brief commit pause, connection drain, replica catch-up, trigger lag, cache invalidation vagy application retry storm. Define-old tolerable interruptiont, measure actual cutover durationt, és explicit módon kommunikáld a residual outage risk-et.

## Források
- [MySQL — ALTER TABLE](https://dev.mysql.com/doc/refman/8.4/en/alter-table.html)
- [PostgreSQL — SQL Commands](https://www.postgresql.org/docs/current/sql-commands.html)
