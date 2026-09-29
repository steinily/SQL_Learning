---
schema_version: 1
id: DBKB-REC-0010
title: Observability Recipes
type: playbook
primary_domain: recipes
secondary_domains: [observability, operations]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql, sqlite]
sql_dialects: [postgresql, tsql, mysql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-REC-0009]
related: [DBKB-OBS-0001]
aliases: [database monitoring recipe]
search_keywords: [database metrics, slow query, lock wait, replication lag, alert]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-RECIPES-0001]
source_ids: [SRC-000001, SRC-000086]
acceptance_criteria: [Golden signals, query/lock/replication metrics, alert ownership and evidence are defined]
---
# Observability Recipes

Collect request throughput/error/latency, connection pool, CPU/memory/disk, lock wait/deadlock, cache hit, query plan/scan, replication lag, backup freshness és data quality signals. Tag metrics database/tenant/workload és sensitive payload nélkül.

Alerthez threshold, duration, owner, escalation, dedup/suppression és runbook link kell. Incident alatt capture-öld timestamp, query fingerprint, transaction/session, plan, lock graph és change correlation; dashboard aggregate ne rejtse el a hot shardot.

## Források
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [Apache Cassandra Documentation](https://cassandra.apache.org/doc/latest/)
