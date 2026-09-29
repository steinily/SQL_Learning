---
schema_version: 1
id: DBKB-PG-0029
title: Streaming Replication
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
prerequisites: [DBKB-PG-0028]
related: [DBKB-PG-0030]
aliases: [physical streaming replication]
search_keywords: [streaming replication, standby, WAL receiver, replication lag]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-PG-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Primary/standby, sync/async, lag és failover caveat-et adja]
---
# Streaming Replication

Streaming replication WAL recordsot továbbít primaryból standbyba, szinkron vagy aszinkron commit policy mellett. Receive/replay lag, synchronous quorum és failover readiness külön mérendő; standby read-only nem automatikusan failover-safe.

## Források
- [PostgreSQL 18 — Streaming Replication](https://www.postgresql.org/docs/18/warm-standby.html)
