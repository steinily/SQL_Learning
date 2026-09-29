---
schema_version: 1
id: DBKB-RDBE-0020
title: Relational Engineering Exercise
type: exercise
primary_domain: relational-database-engineering
secondary_domains: [migrations, data-integrity]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [sqlite]
sql_dialects: [portable-sql, sqlite]
scope: portable-sql
prerequisites: [DBKB-RDBE-0002, DBKB-RDBE-0003, DBKB-RDBE-0015]
related: [DBKB-RDBE-0019]
aliases: [DDL exercise]
search_keywords: [exercise, ddl, constraint, view, migration, review]
risk: caution
version_sensitive: false
review_cycle: 24m
research_packages: [RP-RDBE-0001]
source_ids: [SRC-000009]
acceptance_criteria: [Feladatot és DDL safety evidence-et ad, Constraint/view/rollback kérdéseket lefedi]
---
# Relational Engineering Exercise

Hozz létre customer és order table-t primary key, non-null foreign key és pozitív amount constrainttel.
Készíts explicit-column view-t, majd tervezz additive migrationt egy új status columnhoz.

Leadandó evidence: valid és invalid insert; view result; precondition/postcondition; expected affected
row count; lock/dependency analysis; rollback vagy forward-repair út; owner és next review.

A feladat célja nem a DDL mennyisége, hanem az executable contract és a változtatás biztonságának
bizonyítása.

## Források

- [PostgreSQL 18 — Constraints](https://www.postgresql.org/docs/18/ddl-constraints.html)
