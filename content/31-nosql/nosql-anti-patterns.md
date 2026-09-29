---
schema_version: 1
id: DBKB-NOSQL-0022
title: NoSQL Anti-Patterns
type: error
primary_domain: nosql
secondary_domains: [data-modeling, operations]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [mongodb, redis, apache-cassandra, apache-couchdb]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-NOSQL-0021]
related: [DBKB-NOSQL-0006, DBKB-NOSQL-0013]
aliases: [NoSQL mistakes]
search_keywords: [hot partition, unbounded scan, cache as source of truth, schema drift]
risk: production-critical
version_sensitive: false
review_cycle: 12m
research_packages: [RP-NOSQL-0001]
source_ids: [SRC-000086, SRC-000089, SRC-000090, SRC-000091]
acceptance_criteria: [Common modeling and operations anti-patterns include mitigations]
---
# NoSQL Anti-Patterns

Gyakori hiba: relational schema vak másolása, unbounded partition/document, rossz shard key, cross-shard scan, uncontrolled secondary index és cache source-of-truth-ként kezelése.

További veszély a mixed schema validation nélkül, silent conflict overwrite, infinite retry, backup restore drill hiánya és vendor feature execution nélkül történő állítása. Minden anti-patternhez legyen detection metric, bounded remediation és rollback.

## Források
- [MongoDB Manual](https://www.mongodb.com/docs/manual/)
- [Redis Documentation](https://redis.io/docs/latest/)
- [Apache Cassandra Documentation](https://cassandra.apache.org/doc/latest/)
- [Apache CouchDB Documentation](https://docs.couchdb.org/)
