---
schema_version: 1
id: DBKB-MODL-0012
title: Hierarchy Modeling
type: concept
primary_domain: data-modeling
secondary_domains: [relational-design]
levels: [intermediate, advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql, sqlite]
sql_dialects: [portable-sql, postgresql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-MODL-0004, DBKB-ISQL-0022]
related: [DBKB-ASQL-0016]
aliases: [tree model, adjacency list]
search_keywords: [hierarchy, parent_id, tree, closure table, path]
risk: caution
version_sensitive: false
review_cycle: 12m
research_packages: [RP-MODL-0002]
source_ids: [SRC-000009]
acceptance_criteria: [Adjacency list és closure/path trade-offot összevet, Cycle és orphan policyt ad]
---
# Hierarchy Modeling

Adjacency list `parent_id`-val egyszerűen írható és FK-val integrityt kap, de descendant queryhez
recursive traversal kell. Closure table minden ancestor-descendant párt tárol, gyors olvasást, több
write-ot és cycle preventiont igényel. Materialized path olvasható, de path update és escaping
kockázatot hoz.

Döntsd el, tree vagy általános graph kell-e; root, orphan, multiple-parent és cycle szabály legyen
explicit. Tenant és temporal scope-ot a hierarchy key-be is be kell venni, ha ezek szerint izolált.

## Források

- [PostgreSQL 18 — Constraints](https://www.postgresql.org/docs/18/ddl-constraints.html)
