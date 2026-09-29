---
schema_version: 1
id: DBKB-OBS-0006
title: Golden Signals for Database Services
type: concept
primary_domain: observability
secondary_domains: [reliability]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql, prometheus]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-OBS-0003]
related: []
aliases: [database golden signals]
search_keywords: [latency, traffic, errors, saturation, golden signals]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-OBS-0001]
source_ids: [SRC-000054, SRC-000056]
acceptance_criteria: [Signal dimensions and actionable interpretation are defined]
---
# Golden Signals for Database Services

Database service-nél a latency, traffic, errors és saturation jelek engine-specific counters-szel egészülnek ki: lock wait, connection exhaustion, replication lag vagy storage headroom. A signal target, aggregation és window legyen explicit, különben a dashboard trendje nem vezethető vissza user impactre.

## Források
- [Prometheus Documentation](https://prometheus.io/docs/)
- [PostgreSQL — Monitoring Database Activity](https://www.postgresql.org/docs/current/monitoring.html)
