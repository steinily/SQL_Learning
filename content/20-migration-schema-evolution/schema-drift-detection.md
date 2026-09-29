---
schema_version: 1
id: DBKB-MIG-0017
title: Schema Drift Detection
type: technology
primary_domain: migration
secondary_domains: [observability, governance]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-MIG-0016]
related: []
aliases: [database schema drift]
search_keywords: [schema drift, desired state, metadata diff, unauthorized change]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-MIG-0001]
source_ids: [SRC-000060, SRC-000061, SRC-000062]
acceptance_criteria: [Desired state, diff classification and remediation evidence are defined]
---
# Schema Drift Detection

Drift detection desired schema state-et hasonlít effective metadatahoz, és külön jelöli intentional, emergency, tool-generated és unauthorized változásokat. Compare algoritmusnak kezelnie kell engine defaults, ordering, generated objects, collation és permission differences; remediation előtt owner review kell.

## Források
- [PostgreSQL — SQL Commands](https://www.postgresql.org/docs/current/sql-commands.html)
