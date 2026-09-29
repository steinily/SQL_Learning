---
schema_version: 1
id: DBKB-NOSQL-0006
title: NoSQL Data Modeling
type: concept
primary_domain: nosql
secondary_domains: [data-modeling, architecture]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [mongodb, redis, apache-cassandra, apache-couchdb]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-NOSQL-0005]
related: [DBKB-NOSQL-0007, DBKB-DDS-0003]
aliases: [access-pattern modeling]
search_keywords: [NoSQL modeling, access pattern, aggregate, partition key]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-NOSQL-0001]
source_ids: [SRC-000086, SRC-000089, SRC-000090, SRC-000091]
acceptance_criteria: [Access-pattern-first modeling, aggregate boundaries and operational constraints are explained]
---
# NoSQL Data Modeling

NoSQL modellezésnél az access pattern az első input: melyik key alapján, milyen bounded resulttal, milyen latency/SLO mellett olvasol és írsz. Ebből következik az aggregate boundary, partition/shard key, index és denormalized projection.

Minden duplicate fieldhez legyen update owner és repair path. Rögzítsd a maximum document/partition méretet, hot-key kockázatot, cardinality-t, retentiont és schema evolution szabályt.

## Források
- [Apache Cassandra Documentation](https://cassandra.apache.org/doc/latest/)
- [MongoDB Manual](https://www.mongodb.com/docs/manual/)
- [Redis Documentation](https://redis.io/docs/latest/)
- [Apache CouchDB Documentation](https://docs.couchdb.org/)
