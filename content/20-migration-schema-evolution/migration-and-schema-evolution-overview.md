---
schema_version: 1
id: DBKB-MIG-0001
title: Migration and Schema Evolution Overview
type: overview
primary_domain: migration
secondary_domains: [database-operations, deployment]
levels: [beginner]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-TEST-0015]
related: []
aliases: [database migration overview]
search_keywords: [schema evolution, migration, compatibility, rollout]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-MIG-0001]
source_ids: [SRC-000060, SRC-000061, SRC-000062]
acceptance_criteria: [Migration lifecycle, compatibility and evidence are defined]
---
# Migration and Schema Evolution Overview

Schema evolution a database structure, data, application contract és operational behavior kontrollált változtatása. A safe migration célja nem pusztán a DDL success, hanem kompatibilis rollout, bounded lock/rewrite impact, verified data state és visszaállítható release path.

## Források
- [PostgreSQL — SQL Commands](https://www.postgresql.org/docs/current/sql-commands.html)
- [MySQL — ALTER TABLE](https://dev.mysql.com/doc/refman/8.4/en/alter-table.html)
