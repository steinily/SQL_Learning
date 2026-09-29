---
schema_version: 1
id: DBKB-PG-0027
title: Upgrade Strategies
type: playbook
primary_domain: postgresql
secondary_domains: [operations]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-PG-0003, DBKB-PG-0004]
related: [DBKB-PG-0039]
aliases: [major upgrade, minor upgrade]
search_keywords: [PostgreSQL upgrade, pg_upgrade, logical replication upgrade]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-PG-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Minor/major upgrade, compatibility, downtime és rollback trade-offot adja]
---
# Upgrade Strategies

Minor release upgrade általában binary/package change; major upgrade külön compatibility, catalog és migration tervet igényel. `pg_upgrade`, dump/restore és logical replication eltérő downtime, risk és rollback modellt ad; rehearsal és restore evidence szükséges.

## Források
- [PostgreSQL 18 — Upgrading a PostgreSQL Cluster](https://www.postgresql.org/docs/18/upgrading.html)
