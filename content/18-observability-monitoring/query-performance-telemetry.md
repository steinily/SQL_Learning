---
schema_version: 1
id: DBKB-OBS-0010
title: Query Performance Telemetry
type: technology
primary_domain: observability
secondary_domains: [performance]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-OBS-0003]
related: []
aliases: [database query telemetry]
search_keywords: [query latency, query fingerprint, execution statistics, slow query]
risk: caution
version_sensitive: true
review_cycle: 6m
research_packages: [RP-OBS-0001]
source_ids: [SRC-000054]
acceptance_criteria: [Query telemetry, privacy and overhead trade-offs are stated]
---
# Query Performance Telemetry

Query telemetryben fingerprint, latency distribution, execution count, rows, error rate és resource usage legyen elérhető. Raw SQL és bind values exportja privacy/cardinality risk; redaction, aggregation, sampling és collection overhead mérés nélkül a telemetry maga is production risk.

## Források
- [PostgreSQL — Monitoring Database Activity](https://www.postgresql.org/docs/current/monitoring.html)
