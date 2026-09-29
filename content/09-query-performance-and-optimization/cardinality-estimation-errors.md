---
schema_version: 1
id: DBKB-PERF-0013
title: Cardinality Estimation Errors
type: troubleshooting
primary_domain: query-performance
secondary_domains: [postgresql]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-PERF-0005, DBKB-IDX-0011]
related: [DBKB-PERF-0022]
aliases: [row estimate error]
search_keywords: [cardinality estimate, row estimate, stale statistics]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-PERF-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Estimate mismatch okait és evidence-alapú remediationjét adja]
---
# Cardinality Estimation Errors

Ha estimated és actual rows nagyságrenddel eltér, vizsgáld a statistics freshness-t, correlationt, skewet és predicate formát. `ANALYZE` vagy extended statistics csak evidence alapján legyen remediation, ne reflex.

## Források
- [PostgreSQL 18 — Planner Statistics](https://www.postgresql.org/docs/18/planner-stats.html)
