---
schema_version: 1
id: DBKB-INT-0004
title: Heap Storage
type: technology
primary_domain: database-internals
secondary_domains: [postgresql]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-INT-0003]
related: [DBKB-INT-0011, DBKB-INT-0015]
aliases: [heap relation]
search_keywords: [heap storage, heap tuple, HOT update]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-INT-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Heap tuple és update/vacuum interactiont leírja]
---
# Heap Storage

A heap relation a table tuple versioneit tárolja, nem garantál logical row ordert. Update új tuple versiont hozhat létre, amelyet vacuum és index visibility folyamatok kezelnek; HOT behavior külön PostgreSQL detail.

## Források
- [PostgreSQL 18 — Heap-Only Tuples](https://www.postgresql.org/docs/18/storage-hot.html)
