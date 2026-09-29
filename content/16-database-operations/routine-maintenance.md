---
schema_version: 1
id: DBKB-OPS-0009
title: Routine Maintenance
type: playbook
primary_domain: database-operations
secondary_domains: [performance]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-OPS-0006]
related: []
aliases: [database housekeeping]
search_keywords: [vacuum, statistics, index maintenance, housekeeping]
risk: caution
version_sensitive: true
review_cycle: 6m
research_packages: [RP-OPS-0001]
source_ids: [SRC-000049]
acceptance_criteria: [Maintenance cadence and verification are explained]
---
# Routine Maintenance

Routine maintenance a bloat, statistics, index health, logs, orphaned objects és retention policy állapotát kezeli. Engine-specific scheduler vagy command használata előtt mérd a workload impact-et, a lock behavior-t és a szükséges maintenance window-t.

## Források
- [PostgreSQL — Routine Vacuuming](https://www.postgresql.org/docs/current/routine-vacuuming.html)
