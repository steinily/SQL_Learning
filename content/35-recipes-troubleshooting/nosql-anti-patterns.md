---
schema_version: 1
id: DBKB-REC-0050
title: NoSQL Anti-Patterns
type: error
primary_domain: recipes
secondary_domains: [nosql, data-modeling]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [mongodb, redis, apache-cassandra, apache-couchdb]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-REC-0049]
related: [DBKB-NOSQL-0022]
aliases: [NoSQL mistakes]
search_keywords: [unbounded partition, hot key, cache source of truth, conflict overwrite]
risk: production-critical
version_sensitive: true
review_cycle: 12m
research_packages: [RP-RECIPES-0001]
source_ids: [SRC-000086, SRC-000089, SRC-000090, SRC-000091]
acceptance_criteria: [NoSQL modeling, consistency, migration and recovery anti-patterns are covered]
---
# NoSQL Anti-Patterns

Anti-pattern a relational schema vak másolása, unbounded document/partition, poor shard key, cross-shard scan, index everything, cache source-of-truth, blind conflict overwrite és non-idempotent replay.

Detectáld size/skew, query fan-out, conflict/retry, cache miss/stale, lag és reconciliation metrics alapján. Remediation access-pattern redesign, bounded model, source-of-truth, migration/backfill és restore evidence legyen.

## Források
- [MongoDB Manual](https://www.mongodb.com/docs/manual/)
- [Redis Documentation](https://redis.io/docs/latest/)
- [Apache Cassandra Documentation](https://cassandra.apache.org/doc/latest/)
- [Apache CouchDB Documentation](https://docs.couchdb.org/)
