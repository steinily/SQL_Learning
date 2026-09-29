---
schema_version: 1
id: DBKB-IDX-0016
title: Heap and Index-Only Scans
type: technology
primary_domain: indexing
secondary_domains: [performance]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-IDX-0006]
related: [DBKB-IDX-0013]
aliases: [index-only scan, heap fetch]
search_keywords: [heap scan, index-only scan, visibility map]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-IDX-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Heap fetch és index-only feltételeket visibilityvel magyaráz]
---
# Heap and Index-Only Scans

Index-only scan csak akkor előnyös, ha az index lefedi a lekérdezést és a visibility map alapján a heap fetch elhagyható. `EXPLAIN (ANALYZE, BUFFERS)` segítségével ellenőrizd a tényleges heap access-t.

## Források
- [PostgreSQL 18 — Index-Only Scans](https://www.postgresql.org/docs/18/indexes-index-only-scans.html)
