---
schema_version: 1
id: DBKB-INT-0018
title: Replication Internals
type: technology
primary_domain: database-internals
secondary_domains: [reliability]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-INT-0016]
related: [DBKB-INT-0017]
aliases: [streaming replication, logical replication]
search_keywords: [replication, WAL sender, standby, replication lag]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-INT-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Physical/logical replication boundaryt és lag evidence-et leírja]
---
# Replication Internals

Physical streaming replication WAL recordokat továbbít standby felé; logical replication változásokat publikáció/subscription szemantikával közvetít. Replication lag külön receive, replay és apply komponensekre bontható.

## Források
- [PostgreSQL 18 — Replication](https://www.postgresql.org/docs/18/replication.html)
