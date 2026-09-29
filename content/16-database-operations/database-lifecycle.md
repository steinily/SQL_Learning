---
schema_version: 1
id: DBKB-OPS-0002
title: Database Lifecycle
type: concept
primary_domain: database-operations
secondary_domains: [governance]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-OPS-0001]
related: []
aliases: [database service lifecycle]
search_keywords: [provisioning, operation, decommissioning]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-OPS-0001]
source_ids: [SRC-000049]
acceptance_criteria: [Lifecycle states and exit evidence are explained]
---
# Database Lifecycle

A database service lifecycle-je a design, provision, configure, operate, maintain, upgrade, retire szakaszokat tartalmazza. Minden transitionhöz owner, approval, evidence és visszalépési vagy archiválási terv szükséges.

## Források
- [PostgreSQL — Server Administration](https://www.postgresql.org/docs/current/admin.html)
