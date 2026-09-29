---
schema_version: 1
id: DBKB-OPS-0010
title: Patching and Upgrades
type: playbook
primary_domain: database-operations
secondary_domains: [change-management]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-OPS-0004]
related: []
aliases: [database upgrade runbook]
search_keywords: [patching, major upgrade, compatibility, rollback]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-OPS-0001]
source_ids: [SRC-000049]
acceptance_criteria: [Compatibility, backup, rollout and rollback concerns are listed]
---
# Patching and Upgrades

Patch vagy major upgrade előtt ellenőrizd compatibility matrix-et, extension/driver támogatást, backup restore-olhatóságot és rollback lehetőséget. Staged rollout, health checks és post-upgrade query/application verification szükséges; version change-et ne rejts el konfigurációs módosításként.

## Források
- [PostgreSQL — Upgrading a PostgreSQL Cluster](https://www.postgresql.org/docs/current/upgrading.html)
