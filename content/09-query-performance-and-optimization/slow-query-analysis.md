---
schema_version: 1
id: DBKB-PERF-0026
title: Slow Query Analysis
type: troubleshooting
primary_domain: query-performance
secondary_domains: [operations]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-PERF-0025]
related: [DBKB-PERF-0023]
aliases: [slow query triage]
search_keywords: [slow query, query latency, wait event]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-PERF-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Slow query triage ordert plan, wait, data, resource szerint adja]
---
# Slow Query Analysis

Triage sorrend: query fingerprint és időablak; wait versus CPU/I/O; plan és estimated/actual rows; concurrent load; data és configuration változás. Ne optimalizálj kizárólag a leglassabb egyetlen sample alapján.

## Források
- [PostgreSQL 18 — Monitoring Database Activity](https://www.postgresql.org/docs/18/monitoring.html)
