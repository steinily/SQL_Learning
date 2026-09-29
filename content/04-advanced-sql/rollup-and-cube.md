---
schema_version: 1
id: DBKB-ASQL-0015
title: ROLLUP and CUBE
type: comparison
primary_domain: advanced-sql
secondary_domains: [analytics]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-ASQL-0014]
related: [DBKB-ISQL-0004]
aliases: [hierarchical subtotal, multidimensional subtotal]
search_keywords: [rollup, cube, subtotal, grouping sets]
risk: caution
version_sensitive: true
review_cycle: 6m
research_packages: [RP-ASQL-0002]
source_ids: [SRC-000036]
acceptance_criteria:
  - Összehasonlítja a prefix hierarchy és power-set groupingot.
  - Figyelmeztet a CUBE exponenciális outputjára.
  - PostgreSQL 18 scope-ot és N/A executiont rögzít.
---
# ROLLUP and CUBE

`ROLLUP(a,b,c)` hierarchikus prefix grouping seteket generál: `(a,b,c)`, `(a,b)`, `(a)`, `()`.
`CUBE(a,b,c)` minden combinationt generál, vagyis legfeljebb `2^n` grouping levelt. A column order
`ROLLUP` esetén semantic.

`ROLLUP` természetes region→country→city hierarchyhoz; `CUBE` kis számú, független dimension teljes
cross-summaryjához illik. Nagy dimension-számnál a `CUBE` output és work gyorsan nő, ezért csak
szükséges grouping seteket kérj.

Subtotal `NULL` és stored `NULL` elkülönítéséhez grouping metadata kell. Minden levelhez explicit
label és grain contract szükséges. Final ordering nem implicit hierarchy order.

A feature-t PostgreSQL 18 official source igazolja; a local SQLite környezet nem támogatja ezt a
syntaxot, ezért execution dimenziója őszintén `N/A`.

## Források

- [PostgreSQL 18 — Table Expressions](https://www.postgresql.org/docs/18/queries-table-expressions.html)
