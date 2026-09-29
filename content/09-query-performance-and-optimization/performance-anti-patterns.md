---
schema_version: 1
id: DBKB-PERF-0030
title: Performance Anti-Patterns
type: troubleshooting
primary_domain: query-performance
secondary_domains: [governance]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: cross-vendor
prerequisites: [DBKB-PERF-0023]
related: [DBKB-PERF-0029]
aliases: [query tuning anti-pattern]
search_keywords: [performance anti-pattern, premature optimization, hint abuse]
risk: production-critical
version_sensitive: false
review_cycle: 12m
research_packages: [RP-PERF-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Premature tuning, no baseline, hint abuse és cache warming félreértést felsorol]
---
# Performance Anti-Patterns

Anti-pattern a baseline nélküli tuning, egyetlen query sample túlértelmezése, blanket configuration change, index/hint halmozás és cache warmup production evidence-ként kezelése. Minden változtatásnak legyen mérhető hypothesis-e.

## Források
- [PostgreSQL 18 — Using EXPLAIN](https://www.postgresql.org/docs/18/using-explain.html)
