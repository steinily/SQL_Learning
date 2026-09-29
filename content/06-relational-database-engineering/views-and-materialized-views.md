---
schema_version: 1
id: DBKB-RDBE-0006
title: Views and Materialized Views
type: comparison
primary_domain: relational-database-engineering
secondary_domains: [analytics, security]
levels: [intermediate, advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql, sqlite]
sql_dialects: [postgresql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-ISQL-0024]
related: [DBKB-RDBE-0007]
aliases: [view, materialized view]
search_keywords: [view, materialized view, refresh, abstraction, dependency]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-RDBE-0001]
source_ids: [SRC-000037, SRC-000038]
acceptance_criteria: [Virtual és stored result lifecycle-t összevet, Refresh staleness és dependency policyt ad]
---
# Views and Materialized Views

Normál view named query interface, rendszerint stored result nélkül. Materialized view fizikai resultot
tárol, ezért refresh, staleness, locking, index és failure policy szükséges. View contractot a
consumer által használt columnnév/type/grain adja; `SELECT *` törékeny.

View nem automatikusan security boundary, updatable vagy performance optimization. Materialized result
sem „current” adat refresh evidence nélkül.

A `SQL-RDBE-0006` SQLite view létrehozását és readbackjét ellenőrzi; materialized-view állítások
PostgreSQL source-verifiedek.

## Források

- [PostgreSQL 18 Tutorial — Views](https://www.postgresql.org/docs/18/tutorial-views.html)
- [PostgreSQL 18 — CREATE TABLE](https://www.postgresql.org/docs/18/sql-createtable.html)
