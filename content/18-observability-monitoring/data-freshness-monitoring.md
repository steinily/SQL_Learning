---
schema_version: 1
id: DBKB-OBS-0015
title: Data Freshness Monitoring
type: technology
primary_domain: observability
secondary_domains: [data-quality, reliability]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql, prometheus]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-OBS-0012]
related: []
aliases: [freshness SLA monitoring]
search_keywords: [data freshness, watermark, ingestion lag, staleness]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-OBS-0001]
source_ids: [SRC-000054, SRC-000056]
acceptance_criteria: [Freshness indicator, watermark and alert semantics are defined]
---
# Data Freshness Monitoring

Freshness monitoring a source event time, ingestion time, watermark, processing delay és last-known-good value alapján mérje a staleness-t. A wall-clock timestamp önmagában félrevezető lehet late-arriving data, backfill vagy paused pipeline esetén; policy és expected window legyen explicit.

## Források
- [Prometheus Documentation](https://prometheus.io/docs/)
- [PostgreSQL — Monitoring Database Activity](https://www.postgresql.org/docs/current/monitoring.html)
