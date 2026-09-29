---
schema_version: 1
id: DBKB-PG-0036
title: PostgreSQL Exercise 2
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
prerequisites: [DBKB-PG-0021, DBKB-PG-0030]
related: [DBKB-PG-0038]
aliases: [PostgreSQL security HA lab]
search_keywords: [RLS exercise, failover exercise, PostgreSQL lab]
risk: safe
version_sensitive: true
review_cycle: 12m
research_packages: [RP-PG-0001]
source_ids: [SRC-000014]
acceptance_criteria: [RLS policy és HA drill tervezését gyakoroltatja]
---
# PostgreSQL Exercise 2

Tervezd meg egy tenant-scoped RLS policy és egy controlled failover drill tesztmátrixát. Rögzítsd role contextet, expected visibilityt, promotion criteria-t, client reconnectet és rollbacket; ne állíts tényleges production eredményt.

## Források
- [PostgreSQL 18 — Row Security Policies](https://www.postgresql.org/docs/18/ddl-rowsecurity.html)
