---
schema_version: 1
id: DBKB-MIG-0011
title: Migration Rollback and Roll-forward
type: playbook
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
prerequisites: [DBKB-MIG-0010]
related: []
aliases: [migration recovery plan]
search_keywords: [rollback, roll-forward, revert, restore, abort]
risk: destructive
version_sensitive: true
review_cycle: 6m
research_packages: [RP-MIG-0001]
source_ids: [SRC-000060, SRC-000061, SRC-000062]
acceptance_criteria: [Rollback feasibility, roll-forward and abort decision points are explained]
---
# Migration Rollback and Roll-forward

DDL rollback sokszor nem inverse command: data transform, backfill, concurrent writes és irreversible drop miatt roll-forward corrective migration vagy restore lehet a valódi recovery path. Decision tree, backup point, compatibility window, abort threshold és actual rehearsal legyen dokumentálva.

## Források
- [PostgreSQL — SQL Commands](https://www.postgresql.org/docs/current/sql-commands.html)
- [MySQL — ALTER TABLE](https://dev.mysql.com/doc/refman/8.4/en/alter-table.html)
