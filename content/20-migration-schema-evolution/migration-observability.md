---
schema_version: 1
id: DBKB-MIG-0012
title: Migration Observability
type: technology
primary_domain: migration
secondary_domains: [observability]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql, prometheus]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-MIG-0011]
related: []
aliases: [migration telemetry]
search_keywords: [migration progress, lock wait, error rate, backfill lag]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-MIG-0001]
source_ids: [SRC-000060, SRC-000061, SRC-000062]
acceptance_criteria: [Progress, impact, errors and completion signals are defined]
---
# Migration Observability

Migration telemetryben progress/checkpoint, rows remaining, duration, lock wait, query latency, error/retry, replication lag, application errors és parity/reconciliation állapot legyen. Dashboard és alert scope-ot a migration owner, abort threshold és rollback/roll-forward döntéshez kösd.

## Források
- [PostgreSQL — SQL Commands](https://www.postgresql.org/docs/current/sql-commands.html)
