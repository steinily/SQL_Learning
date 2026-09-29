---
schema_version: 1
id: DBKB-DR-0005
title: Point in Time Recovery
type: technology
primary_domain: backup
secondary_domains: [reliability]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server]
sql_dialects: [postgresql, tsql]
scope: vendor-specific
prerequisites: [DBKB-DR-0004]
related: []
aliases: [PITR]
search_keywords: [point in time recovery, WAL archive, log chain, recovery target]
risk: destructive
version_sensitive: true
review_cycle: 6m
research_packages: [RP-DR-0001]
source_ids: [SRC-000063, SRC-000065]
acceptance_criteria: [PITR prerequisites, target selection and verification are explained]
---
# Point in Time Recovery

PITR continuous archive/log chain, base backup, recovery target, timeline és required keys/storage integrity függvénye. Target timestamp kiválasztása után ellenőrizd transaction/business boundary-t, missing archive-ot, replay completiont és application data correctness-t; sample timeline nem execution evidence.

## Források
- [PostgreSQL — Continuous Archiving and Point-in-Time Recovery](https://www.postgresql.org/docs/current/continuous-archiving.html)
- [Microsoft — Backup and Restore](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/)
