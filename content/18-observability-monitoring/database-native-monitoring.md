---
schema_version: 1
id: DBKB-OBS-0003
title: Database Native Monitoring
type: technology
primary_domain: observability
secondary_domains: [database-operations]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-OBS-0002]
related: []
aliases: [database activity monitoring]
search_keywords: [database statistics, sessions, locks, activity views]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-OBS-0001]
source_ids: [SRC-000054]
acceptance_criteria: [Database-native signals and version caveats are described]
---
# Database Native Monitoring

Database-native monitoring a sessions, queries, locks, transactions, replication, storage és statistics állapotát közvetlenül az engine-ből olvassa. A view schema és counters version-sensitive; collection query-k legyenek read-only, permission-scoped és workload impact alapján limitáltak.

## Források
- [PostgreSQL — Monitoring Database Activity](https://www.postgresql.org/docs/current/monitoring.html)
