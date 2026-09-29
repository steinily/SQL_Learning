---
schema_version: 1
id: DBKB-PG-0035
title: PostgreSQL Exercise 1
type: exercise
primary_domain: postgresql
secondary_domains: [practice]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-PG-0025, DBKB-PG-0031]
related: [DBKB-PG-0039]
aliases: [PostgreSQL operations lab]
search_keywords: [PostgreSQL exercise, backup restore lab, monitoring lab]
risk: safe
version_sensitive: true
review_cycle: 12m
research_packages: [RP-PG-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Monitoring snapshot, backup inventory és restore validation feladatot adja]
---
# PostgreSQL Exercise 1

Készíts staging lab reportot: query/activity snapshot, backup inventory, WAL archive health és restore verification. Minden resulthez írd hozzá PostgreSQL versiont, configurationt, timestampet és environment scope-ot.

## Források
- [PostgreSQL 18 — Backup and Restore](https://www.postgresql.org/docs/18/backup.html)
