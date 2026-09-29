---
schema_version: 1
id: DBKB-PERF-0032
title: Plan Reading Exercise
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
prerequisites: [DBKB-PERF-0004, DBKB-PERF-0013]
related: [DBKB-PERF-0031]
aliases: [execution plan lab]
search_keywords: [plan reading, estimated rows, actual rows]
risk: safe
version_sensitive: true
review_cycle: 12m
research_packages: [RP-PERF-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Plan node tree, row mismatch és bottleneck azonosítást gyakoroltat]
---
# Plan Reading Exercise

Jelöld ki a plan tree legnagyobb estimated/actual rows eltérését, a legtöbb buffer readet és a domináns elapsed node-ot. Válaszd el a root cause-ot a downstream tünettől, és támassz alá minden állítást outputtal.

## Források
- [PostgreSQL 18 — Using EXPLAIN](https://www.postgresql.org/docs/18/using-explain.html)
