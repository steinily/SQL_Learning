---
schema_version: 1
id: DBKB-IDX-0017
title: Bitmap Index Scans
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
prerequisites: [DBKB-IDX-0016]
related: [DBKB-IDX-0010]
aliases: [bitmap heap scan]
search_keywords: [bitmap index scan, bitmap heap scan, planner]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-IDX-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Bitmap scan és heap recheck plan behaviorét megmagyarázza]
---
# Bitmap Index Scans

PostgreSQL bitmap planban indexből bitmap készül, majd heap blokkok olvasása történik; több index feltételei is kombinálhatók. A tényleges választást `EXPLAIN` outputtal validáld, ne az index jelenlétéből következtesd.

## Források
- [PostgreSQL 18 — Combining Multiple Indexes](https://www.postgresql.org/docs/18/indexes-bitmap-scans.html)
