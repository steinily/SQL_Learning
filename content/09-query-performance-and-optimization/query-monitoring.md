---
schema_version: 1
id: DBKB-PERF-0025
title: Query Monitoring
type: technology
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
prerequisites: [DBKB-PERF-0024]
related: [DBKB-PERF-0026]
aliases: [query observability]
search_keywords: [query monitoring, pg_stat_statements, active query]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-PERF-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Query monitoring signaleket és privacy caveat-et ad]
---
# Query Monitoring

Monitorozd a query countot, total és mean time-ot, rows, calls, errors, wait eventet és resource contextet. Query text és bind values kezelése privacy-sensitive lehet; a monitoring retention és access policy legyen explicit.

## Források
- [PostgreSQL 18 — The Statistics Collector](https://www.postgresql.org/docs/18/monitoring-stats.html)
