---
schema_version: 1
id: DBKB-INT-0002
title: Storage Engine Concepts
type: concept
primary_domain: database-internals
secondary_domains: [storage]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-INT-0001]
related: [DBKB-INT-0003, DBKB-INT-0007]
aliases: [storage manager]
search_keywords: [storage engine, page layout, buffer manager]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-INT-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Storage manager, buffer manager és durability kapcsolatát definiálja]
---
# Storage Engine Concepts

Storage engine a logical row műveleteket pages, tuple versions, indexes, buffers és durable files műveleteire fordítja. A performance és recovery behavior ezek interakciójából ered; engine-specific dokumentáció szükséges.

## Források
- [PostgreSQL 18 — Database Physical Storage](https://www.postgresql.org/docs/18/storage.html)
