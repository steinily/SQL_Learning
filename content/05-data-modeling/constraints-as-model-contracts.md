---
schema_version: 1
id: DBKB-MODL-0019
title: Constraints as Model Contracts
type: concept
primary_domain: data-modeling
secondary_domains: [data-integrity]
levels: [intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql, sqlite]
sql_dialects: [portable-sql, postgresql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-FND-0010, DBKB-MODL-0004]
related: [DBKB-MODL-0009, DBKB-MODL-0023]
aliases: [schema invariant]
search_keywords: [primary key, foreign key, check, not null, unique]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-MODL-0003]
source_ids: [SRC-000009]
acceptance_criteria: [Constraint típusokat és enforcement felelősséget felsorol, Migration/backfill kockázatot ad]
---
# Constraints as Model Contracts

Constraint executable model contract: `NOT NULL` required value-t, `CHECK` domain predicateet,
`UNIQUE` uniquenesset, primary key identityt, foreign key referential integrityt fejez ki. A
constraint minden writerre érvényes, ezért erősebb boundary, mint application-only validation.

Constraint deployment dirty data, lock, deferrability és migration ordering kérdéseket hozhat. Új
constraint előtt profile, validate és backfill szükséges. Engine-specific timingot ne generalizálj.

## Források

- [PostgreSQL 18 — Constraints](https://www.postgresql.org/docs/18/ddl-constraints.html)
