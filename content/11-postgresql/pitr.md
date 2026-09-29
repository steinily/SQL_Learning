---
schema_version: 1
id: DBKB-PG-0032
title: PITR
type: technology
primary_domain: postgresql
secondary_domains: [reliability]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-PG-0031]
related: [DBKB-INT-0016]
aliases: [point-in-time recovery]
search_keywords: [PITR, recovery target, WAL restore]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-PG-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Base backup + WAL, recovery target és verification folyamatot adja]
---
# PITR

Point-in-time recovery base backupot és folytonos WAL archivingot kombinál, hogy egy recovery target időpontig állítsa vissza a cluster állapotát. Target kiválasztás, timeline, missing WAL és application consistency külön ellenőrzendő.

## Források
- [PostgreSQL 18 — Continuous Archiving and PITR](https://www.postgresql.org/docs/18/continuous-archiving.html)
