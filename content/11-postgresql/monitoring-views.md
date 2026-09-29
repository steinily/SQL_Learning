---
schema_version: 1
id: DBKB-PG-0025
title: Monitoring Views
type: reference
primary_domain: postgresql
secondary_domains: [observability]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-PG-0024]
related: [DBKB-INT-0021]
aliases: [pg_stat views]
search_keywords: [pg_stat_activity, pg_stat_database, PostgreSQL monitoring views]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-PG-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Activity, database, replication és statistics views purpose-át sorolja]
---
# Monitoring Views

`pg_stat_activity`, `pg_stat_database` és replication/statistics views aktuális session, database és workload signaleket adnak. Snapshot timing, privilege és reset semantics miatt timestamp és query context nélkül ne állíts történeti tényt.

## Források
- [PostgreSQL 18 — Monitoring Database Activity](https://www.postgresql.org/docs/18/monitoring.html)
