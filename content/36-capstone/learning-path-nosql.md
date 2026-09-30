---
schema_version: 1
id: DBKB-CAP-0082
title: Learning Path NoSQL
type: learning-path
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
prerequisites: [DBKB-CAP-0081]
related: [DBKB-CAP-0042, DBKB-CAP-0065]
aliases: [NoSQL learning path]
search_keywords: [NoSQL learning path, document, key value, partition, consistency, migration]
risk: production-critical
version_sensitive: true
review_cycle: 12m
research_packages: [RP-CAPSTONE-0001]
source_ids: [SRC-000086, SRC-000089, SRC-000090, SRC-000091]
acceptance_criteria: [Ordered NoSQL path with model, query, consistency, migration and recovery milestones]
---
# Learning Path NoSQL

Sorrend: data model/access pattern → document/key-value/wide-column/graph → partition/index → consistency/transaction → replication/conflict → schema evolution/backup → NoSQL case/exercise/reference.

Exit criteria: model decision matrix, bounded query, consistency contract, migration, security, restore és reconciliation evidence.

## Források
- [MongoDB Manual](https://www.mongodb.com/docs/manual/)
- [Redis Documentation](https://redis.io/docs/latest/)
- [Apache Cassandra Documentation](https://cassandra.apache.org/doc/latest/)
- [Apache CouchDB Documentation](https://docs.couchdb.org/)
