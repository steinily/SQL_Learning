---
schema_version: 1
id: DBKB-RDBE-0012
title: Object Dependencies
type: concept
primary_domain: relational-database-engineering
secondary_domains: [governance, migrations]
levels: [intermediate, advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-RDBE-0006, DBKB-RDBE-0008]
related: [DBKB-RDBE-0015, DBKB-MODL-0023]
aliases: [schema dependency graph]
search_keywords: [dependency, view, function, foreign key, impact analysis]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-RDBE-0001]
source_ids: [SRC-000009, SRC-000037]
acceptance_criteria: [Dependency graph és change impact fogalmát adja, Drop/rename kockázatot kezeli]
---
# Object Dependencies

Table, column, constraint, view, function, index és application query dependency graphot alkot. DDL
change előtt impact analysis kell: direct és transitive consumer, deployment order, rollback és data
compatibility.

`DROP`, rename vagy type change nem csak a target objectet érinti. View contract, foreign key és
generated expression külön dependency edge. Catalog inspection és repository search együtt szükséges,
mert database metadata nem lát minden external consumer-t.

## Források

- [PostgreSQL 18 Tutorial — Views](https://www.postgresql.org/docs/18/tutorial-views.html)
- [PostgreSQL 18 — Constraints](https://www.postgresql.org/docs/18/ddl-constraints.html)
