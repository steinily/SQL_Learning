---
schema_version: 1
id: DBKB-PERF-0031
title: Query Tuning Exercise
type: exercise
primary_domain: query-performance
secondary_domains: [practice]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-PERF-0003, DBKB-PERF-0023]
related: [DBKB-PERF-0032]
aliases: [query optimization lab]
search_keywords: [query tuning exercise, EXPLAIN ANALYZE lab]
risk: safe
version_sensitive: true
review_cycle: 12m
research_packages: [RP-PERF-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Baseline, hypothesis, plan change és after measurement lépéseit gyakoroltat]
---
# Query Tuning Exercise

Rögzíts baseline `EXPLAIN (ANALYZE, BUFFERS)` outputot, fogalmazz egy hypothesis-t, változtass egy tényezőt, majd hasonlítsd össze a representative runokat. A report tartalmazza a rollbacket és az uncertainty-t.

## Források
- [PostgreSQL 18 — Using EXPLAIN](https://www.postgresql.org/docs/18/using-explain.html)
