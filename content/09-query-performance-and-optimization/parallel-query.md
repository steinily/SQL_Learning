---
schema_version: 1
id: DBKB-PERF-0019
title: Parallel Query
type: technology
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
prerequisites: [DBKB-PERF-0004]
related: [DBKB-PERF-0024]
aliases: [parallel plan]
search_keywords: [parallel query, workers, gather]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-PERF-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Parallel worker overhead és plan evidence caveat-et ad]
---
# Parallel Query

Parallel plan worker process-ekkel osztja meg a scan vagy aggregate munkát, de setup, coordination és contention costot is ad. Worker count és actual rows alapján kell megítélni, nem pusztán a `Gather` jelenlétéből.

## Források
- [PostgreSQL 18 — Parallel Query](https://www.postgresql.org/docs/18/parallel-query.html)
