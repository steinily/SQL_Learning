---
schema_version: 1
id: DBKB-PERF-0011
title: Merge Joins
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
related: [DBKB-PERF-0012, DBKB-PERF-0020]
aliases: [merge join plan]
search_keywords: [merge join, sorted input, join ordering]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-PERF-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Merge join sorted input követelményét és sort costját leírja]
---
# Merge Joins

Merge join két join key szerint rendezett inputot jár be. A már rendezett index vagy előző node csökkentheti a sort costot; különben az ordering előállítása dominálhat.

## Források
- [PostgreSQL 18 — Merge Join](https://www.postgresql.org/docs/18/using-explain.html)
