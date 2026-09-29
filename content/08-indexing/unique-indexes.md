---
schema_version: 1
id: DBKB-IDX-0009
title: Unique Indexes
type: concept
primary_domain: indexing
secondary_domains: [data-integrity]
levels: [intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: cross-vendor
prerequisites: [DBKB-IDX-0003]
related: [DBKB-IDX-0019]
aliases: [unique constraint index]
search_keywords: [unique index, uniqueness constraint]
risk: production-critical
version_sensitive: false
review_cycle: 12m
research_packages: [RP-IDX-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Uniqueness és index implementation kapcsolatát tisztázza]
---
# Unique Indexes

Unique index a duplicate key értékeket tiltó enforcement mechanism lehet. A uniqueness szemantikája NULL-kezelésben és deferrabilityben engine-specific; az üzleti invariantot constraintként dokumentáld.

## Források
- [PostgreSQL 18 — Unique Indexes](https://www.postgresql.org/docs/18/indexes-unique.html)
