---
schema_version: 1
id: DBKB-CAP-0042
title: NoSQL Exercise
type: exercise
primary_domain: capstone
secondary_domains: [nosql, data-modeling]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [mongodb, redis, apache-cassandra, apache-couchdb]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-CAP-0041]
related: [DBKB-NOSQL-0001]
aliases: [NoSQL lab]
search_keywords: [NoSQL exercise, model, partition, consistency, backup]
risk: production-critical
version_sensitive: true
review_cycle: 12m
research_packages: [RP-CAPSTONE-0001]
source_ids: [SRC-000086, SRC-000089, SRC-000090, SRC-000091]
acceptance_criteria: [Learner compares models, query paths, consistency, migration and recovery controls]
---
# NoSQL Exercise

Válassz document, key-value és wide-column modellt egy session/profile workloadhoz. Dokumentáld access pattern, key/index, size/skew, consistency, transaction, TTL/replication és cost trade-offot.

Készíts schema evolution, hot-key/failure, backup/restore és reconciliation test plan-t. Vendor-specific claimet exact release docs és actual output alapján jelölj.

## Források
- [MongoDB Manual](https://www.mongodb.com/docs/manual/)
- [Redis Documentation](https://redis.io/docs/latest/)
- [Apache Cassandra Documentation](https://cassandra.apache.org/doc/latest/)
- [Apache CouchDB Documentation](https://docs.couchdb.org/)
