---
schema_version: 1
id: DBKB-PERF-0004
title: Query Plan Nodes
type: reference
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
prerequisites: [DBKB-PERF-0002]
related: [DBKB-PERF-0006, DBKB-PERF-0010]
aliases: [plan operators]
search_keywords: [plan node, scan node, join node]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-PERF-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Scan, join és sort nodeokat estimated/actual kontextusban sorolja]
---
# Query Plan Nodes

Plan node lehet scan, join, sort, aggregate vagy materialize művelet. Egy node költségét a children, estimated rows, width és actual execution együtt adja; izolált cost-szám nem diagnózis.

## Források
- [PostgreSQL 18 — Using EXPLAIN](https://www.postgresql.org/docs/18/using-explain.html)
