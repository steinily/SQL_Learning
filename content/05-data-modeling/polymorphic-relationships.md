---
schema_version: 1
id: DBKB-MODL-0013
title: Polymorphic Relationships
type: comparison
primary_domain: data-modeling
secondary_domains: [relational-design, data-integrity]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [portable-sql, postgresql]
scope: cross-vendor
prerequisites: [DBKB-MODL-0004, DBKB-MODL-0021]
related: [DBKB-MODL-0015]
aliases: [generic foreign key]
search_keywords: [polymorphic association, generic foreign key, subtype]
risk: caution
version_sensitive: false
review_cycle: 12m
research_packages: [RP-MODL-0002, RP-MODL-0003]
source_ids: [SRC-000009]
acceptance_criteria: [Generic FK integrity kockázatot mutat, Subtype és association-table alternatívát ad]
---
# Polymorphic Relationships

Polymorphic association egy row-t több lehetséges target type-hoz köt, például `(target_type,
target_id)`. Ez rugalmas, de a database rendszerint nem tud egyetlen FK-val minden target table-t
validálni; orphan és cross-type collision kockázat keletkezik.

Alternatíva explicit subtype table, közös supertype key vagy külön association table minden targethez.
Választásnál a query shape, constraint enforcement, migration és ownership a döntő, nem a kevesebb
table.

## Források

- [PostgreSQL 18 — Constraints](https://www.postgresql.org/docs/18/ddl-constraints.html)
