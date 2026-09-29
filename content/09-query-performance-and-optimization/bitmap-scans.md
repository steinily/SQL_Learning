---
schema_version: 1
id: DBKB-PERF-0008
title: Bitmap Scans
type: concept
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
prerequisites: [DBKB-PERF-0007]
related: [DBKB-IDX-0017]
aliases: [bitmap heap scan]
search_keywords: [bitmap scan, bitmap heap scan, recheck]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-PERF-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Bitmap plan szerepét estimated és actual outputtal magyarázza]
---
# Bitmap Scans

Bitmap scan indexből összegyűjtött tuple-helyeket heap blokk-sorrendben olvashat. Ez több predicate kombinációjára is alkalmas lehet; actual buffers és recheck adatok nélkül ne ítéld meg a hatását.

## Források
- [PostgreSQL 18 — Combining Multiple Indexes](https://www.postgresql.org/docs/18/indexes-bitmap-scans.html)
