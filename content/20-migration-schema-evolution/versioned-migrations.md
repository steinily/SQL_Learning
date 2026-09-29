---
schema_version: 1
id: DBKB-MIG-0003
title: Versioned Migrations
type: technology
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
prerequisites: [DBKB-MIG-0002]
related: []
aliases: [migration versioning]
search_keywords: [versioned migration, migration history, checksum, ordering]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-MIG-0001]
source_ids: [SRC-000060]
acceptance_criteria: [Identity, ordering, checksum and applied-state semantics are described]
---
# Versioned Migrations

Versioned migrationhez immutable identifier, ordered dependency, checksum vagy content identity, applied state és environment evidence kell. Existing migration módosítása helyett új corrective migrationt használj, kivéve explicit controlled repair procedure mellett.

## Források
- [PostgreSQL — SQL Commands](https://www.postgresql.org/docs/current/sql-commands.html)
