---
schema_version: 1
id: DBKB-RDBE-0003
title: Constraints and Referential Actions
type: concept
primary_domain: relational-database-engineering
secondary_domains: [data-integrity]
levels: [intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql, sqlite]
sql_dialects: [portable-sql, postgresql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-MODL-0019, DBKB-MODL-0004]
related: [DBKB-RDBE-0016]
aliases: [foreign key actions]
search_keywords: [check, not null, unique, foreign key, cascade, restrict]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-RDBE-0001]
source_ids: [SRC-000009]
acceptance_criteria: [Constraint és referential action semanticsét különít el, Destructive cascade kockázatot ad]
---
# Constraints and Referential Actions

`CHECK`, `NOT NULL`, `UNIQUE`, primary key és foreign key executable invariants. Referential action
(`CASCADE`, `RESTRICT`, `SET NULL`, `SET DEFAULT`) a parent lifecycle változását propagálhatja; ezt
üzleti policyként review-olni kell.

Cascade nem automatikus convenience: nagy graphon sok row-t módosíthat és audit/retention policyt
sérthet. `SET NULL` csak optional relationshipnél értelmes. Constraint addition dirty data, locking
és validation ordering kérdést hoz.

A `SQL-RDBE-0003` invalid foreign key és valid parent delete policy fixture-t futtat SQLite-on.

## Források

- [PostgreSQL 18 — Constraints](https://www.postgresql.org/docs/18/ddl-constraints.html)
