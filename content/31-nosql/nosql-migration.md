---
schema_version: 1
id: DBKB-NOSQL-0023
title: NoSQL Migration
type: playbook
primary_domain: nosql
secondary_domains: [migration, operations]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [mongodb, redis, apache-cassandra, apache-couchdb]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-NOSQL-0022]
related: [DBKB-MIG-0001]
aliases: [NoSQL cutover]
search_keywords: [NoSQL migration, dual write, backfill, cutover, reconciliation]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-NOSQL-0001]
source_ids: [SRC-000086, SRC-000089, SRC-000090, SRC-000091]
acceptance_criteria: [Inventory, dual-run, backfill, cutover, rollback and reconciliation are defined]
---
# NoSQL Migration

Migration előtt inventoryzd a source schema/volume/cardinality/retentiont és a target access pattern/consistency contractot. Válassz snapshot, CDC, dual-write vagy staged backfill stratégiát, és rögzítsd a idempotency/replay szabályt.

Cutover előtt compare count, checksum, sample business invariant és latency/error SLO alapján. A rollback boundary legyen explicit; dual-write drift vagy partial backfill esetén állítsd meg a cutovert, ne takard el a különbséget egy újabb write-tal.

## Források
- [MongoDB Manual](https://www.mongodb.com/docs/manual/)
- [Redis Documentation](https://redis.io/docs/latest/)
- [Apache Cassandra Documentation](https://cassandra.apache.org/doc/latest/)
- [Apache CouchDB Documentation](https://docs.couchdb.org/)
