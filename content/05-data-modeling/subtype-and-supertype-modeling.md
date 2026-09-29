---
schema_version: 1
id: DBKB-MODL-0021
title: Subtype and Supertype Modeling
type: concept
primary_domain: data-modeling
secondary_domains: [relational-design]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [portable-sql, postgresql]
scope: cross-vendor
prerequisites: [DBKB-MODL-0003]
related: [DBKB-MODL-0015]
aliases: [table inheritance, category hierarchy]
search_keywords: [supertype, subtype, discriminator, exclusive, complete]
risk: caution
version_sensitive: false
review_cycle: 12m
research_packages: [RP-MODL-0003]
source_ids: [SRC-000009]
acceptance_criteria: [Table-per-hierarchy, table-per-type és shared-key mintát összevet, Completeness/exclusivity szabályt kezel]
---
# Subtype and Supertype Modeling

Supertype közös identity és attributumokat, subtype specifikus state-et tárol. Megoldás lehet
table-per-hierarchy discriminatorral, table-per-concrete-type, vagy supertype plus shared-key subtype
table. Mindegyik más nullability, join és constraint trade-offot ad.

Rögzítsd, hogy subtype-ok exclusive vagy overlapping, és complete vagy partial category-k. Discriminator
önmagában nem bizonyítja, hogy csak a megfelelő subtype row létezik; FK, check és transaction workflow
kellhet.

## Források

- [PostgreSQL 18 — Constraints](https://www.postgresql.org/docs/18/ddl-constraints.html)
