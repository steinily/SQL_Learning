---
schema_version: 1
id: DBKB-RDBE-0001
title: Relational Database Engineering Overview
type: overview
primary_domain: relational-database-engineering
secondary_domains: [data-modeling, operations]
levels: [intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql, sqlite]
sql_dialects: [portable-sql, postgresql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-MODL-0001, DBKB-SQL-0022]
related: [DBKB-RDBE-0002, DBKB-RDBE-0015]
aliases: [relational engineering]
search_keywords: [table, constraint, view, index, partition, ddl]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-RDBE-0001]
source_ids: [SRC-000009, SRC-000016, SRC-000038]
acceptance_criteria: [A physical engineering lifecycle-t és object ownershipet bemutatja, DDL risket explicitálja]
---
# Relational Database Engineering Overview

Relational database engineering a logical model executable, observable és maintainable physical
objectokra fordítja. Table, constraint, identity, view, index, schema és partition együtt alkotják a
runtime contractot.

Minden DDL változásnál vizsgáld: lock/rewrite, dependency, data backfill, compatibility, rollback,
replication és owner. A physical optimization csak workload evidence után következzen; a correctness
constraint és lifecycle előbbre való.

A portable core és a PostgreSQL-specific feature külön scope-ot kap. SQLite execution csak a deklarált
subsetet bizonyítja.

## Források

- [PostgreSQL 18 — Constraints](https://www.postgresql.org/docs/18/ddl-constraints.html)
- [PostgreSQL 18 — CREATE TABLE](https://www.postgresql.org/docs/18/sql-createtable.html)
