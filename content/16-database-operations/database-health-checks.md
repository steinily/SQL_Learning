---
schema_version: 1
id: DBKB-OPS-0016
title: Database Health Checks
type: reference
primary_domain: database-operations
secondary_domains: [observability]
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
aliases: [database readiness checks]
search_keywords: [health check, readiness, liveness, replication lag]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-OPS-0001]
source_ids: [SRC-000049]
acceptance_criteria: [Health dimensions and false-positive controls are listed]
---
# Database Health Checks

Health check ne csak process liveness legyen: ellenőrizd connectivity, authentication, storage headroom, transaction/lock pressure, replication vagy backup freshness és application query path állapotát. A check legyen timeoutolt, read-only és a dependency failure-t külön jelezze.

## Források
- [PostgreSQL — Monitoring Database Activity](https://www.postgresql.org/docs/current/monitoring.html)
