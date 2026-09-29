---
schema_version: 1
id: DBKB-PERF-0006
title: Sequential Scans
type: concept
primary_domain: query-performance
secondary_domains: [postgresql]
levels: [intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-PERF-0004]
related: [DBKB-IDX-0002]
aliases: [seq scan]
search_keywords: [sequential scan, full table scan]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-PERF-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Sequential scan mikor lehet helyes planner döntés, megmagyarázza]
---
# Sequential Scans

Sequential scan a relation blokkjait sorban olvassa. Nagy result set, kis table vagy alacsony selectivity esetén ez lehet az optimális terv; a `Seq Scan` önmagában nem anti-pattern.

## Források
- [PostgreSQL 18 — Using EXPLAIN](https://www.postgresql.org/docs/18/using-explain.html)
