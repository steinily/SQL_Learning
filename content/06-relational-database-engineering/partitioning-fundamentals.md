---
schema_version: 1
id: DBKB-RDBE-0010
title: Partitioning Fundamentals
type: concept
primary_domain: relational-database-engineering
secondary_domains: [performance, operations]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-MODL-0017, DBKB-RDBE-0002]
related: [DBKB-RDBE-0011, DBKB-RDBE-0018]
aliases: [table partitioning]
search_keywords: [partition, range, list, hash, pruning, retention]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-RDBE-0001]
source_ids: [SRC-000038]
acceptance_criteria: [Partition strategy és key contractot ad, Pruning és maintenance állításokat nem túlgeneralizál]
---
# Partitioning Fundamentals

Partitioning egy logical table-t több physical child relationre bont. Range, list és hash strategy
közül a query/filter, data lifecycle, skew és operational boundary alapján válassz.

Partition key minden insert/update útvonalon értelmezhető legyen; missing/overlap boundary és default
partition külön risk. Partitioning nem automatikus performance win, és nem replacement index.

Maintenance: attach/detach, retention drop, backfill, constraint validation, statistics és backup
rehearsal. Local SQLite nem támogatja a PostgreSQL partition DDL-t, ezért source-verified.

## Források

- [PostgreSQL 18 — CREATE TABLE](https://www.postgresql.org/docs/18/sql-createtable.html)
