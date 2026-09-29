---
schema_version: 1
id: DBKB-PERF-0024
title: Performance Baselines
type: concept
primary_domain: query-performance
secondary_domains: [observability]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: cross-vendor
prerequisites: [DBKB-PERF-0003]
related: [DBKB-PERF-0022]
aliases: [query baseline]
search_keywords: [performance baseline, p95 latency, query baseline]
risk: production-critical
version_sensitive: false
review_cycle: 12m
research_packages: [RP-PERF-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Baseline dimensions, percentile és data context meghatározása]
---
# Performance Baselines

Baseline legyen query fingerprint, dataset/window, engine version, configuration, concurrency és percentile latency alapján definiálva. Átlag önmagában elfedi a tail latency-t és a skewet.

## Források
- [PostgreSQL 18 — Monitoring Database Activity](https://www.postgresql.org/docs/18/monitoring.html)
