---
schema_version: 1
id: DBKB-NOSQL-0011
title: NoSQL Replication
type: technology
primary_domain: nosql
secondary_domains: [distributed-data-systems, availability]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [mongodb, redis, apache-cassandra, apache-couchdb]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-NOSQL-0010]
related: [DBKB-DDS-0004]
aliases: [NoSQL replicas]
search_keywords: [replication, replica lag, failover, conflict resolution]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-NOSQL-0001]
source_ids: [SRC-000086, SRC-000089, SRC-000090, SRC-000091]
acceptance_criteria: [Replica placement, lag, failover and conflict behavior are distinguished]
---
# NoSQL Replication

Replicationnél különítsd el a synchronous/asynchronous acknowledgementet, replica lagot, read routingot és failover ownershipet. A replica count csak akkor ad fault tolerance-t, ha failure domain-ekben helyezkedik el és a recovery procedure bizonyított.

MongoDB replica set, Cassandra replication, Redis replication és CouchDB multi-master replication eltérő semantics-et ad. Dokumentáld a stale read, conflict, write loss és rejoin esetét, majd végezz restore/failover drillt.

## Források
- [MongoDB Manual](https://www.mongodb.com/docs/manual/)
- [Redis Documentation](https://redis.io/docs/latest/)
- [Apache Cassandra Documentation](https://cassandra.apache.org/doc/latest/)
- [Apache CouchDB Documentation](https://docs.couchdb.org/)
