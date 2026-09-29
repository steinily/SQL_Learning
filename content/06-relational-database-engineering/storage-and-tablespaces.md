---
schema_version: 1
id: DBKB-RDBE-0009
title: Storage and Tablespaces
type: concept
primary_domain: relational-database-engineering
secondary_domains: [operations, performance]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-RDBE-0002]
related: [DBKB-RDBE-0010, DBKB-RDBE-0018]
aliases: [storage placement]
search_keywords: [tablespace, storage, disk, capacity, placement]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-RDBE-0001]
source_ids: [SRC-000038]
acceptance_criteria: [Storage placement és logical schema különbségét adja, Capacity/backup/restore impactot rögzít]
---
# Storage and Tablespaces

Tablespace physical storage placementet adhat, míg schema logical namespace. Storage placement nem
helyettesít backup, encryption, capacity monitoring vagy disaster-recovery policyt.

PostgreSQL tablespace path, ownership, permissions, mount availability és restore environment legyen
operational contractban. Object áthelyezés lockot, IO-t és dependency/replication hatást okozhat.

A storage decision workloadból, capacity forecastból és failure domainból induljon; „külön disk gyorsabb”
mérés nélkül nem igazolható. Local SQLite runtime nem modellezi tablespace behavior-t.

## Források

- [PostgreSQL 18 — CREATE TABLE](https://www.postgresql.org/docs/18/sql-createtable.html)
