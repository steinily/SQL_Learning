---
schema_version: 1
id: DBKB-MIG-0002
title: Migration Strategy
type: playbook
primary_domain: migration
secondary_domains: [governance]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-MIG-0001]
related: []
aliases: [schema migration plan]
search_keywords: [migration strategy, rollout, maintenance window, risk]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-MIG-0001]
source_ids: [SRC-000060, SRC-000061, SRC-000062]
acceptance_criteria: [Strategy selection, risk, compatibility and exit criteria are specified]
---
# Migration Strategy

Migration strategy-ban scope, dependency, expected lock/rewrite, data volume, compatibility window, rollout ordering, test evidence, rollback/roll-forward és abort criteria legyen. Target engine version és edition nélkül online vagy zero-downtime állítás nem hitelesíthető.

## Források
- [PostgreSQL — SQL Commands](https://www.postgresql.org/docs/current/sql-commands.html)
- [Microsoft — Modify Columns](https://learn.microsoft.com/en-us/sql/relational-databases/tables/modify-columns-database-engine)
