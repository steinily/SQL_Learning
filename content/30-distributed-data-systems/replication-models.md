---
schema_version: 1
id: DBKB-DDS-0004
title: Replication Models
type: technology
primary_domain: distributed-data-systems
secondary_domains: [availability, operations]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [apache-cassandra, apache-kafka, etcd]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-DDS-0003]
related: [DBKB-DDS-0005, DBKB-DDS-0014]
aliases: [replica placement, replication factor]
search_keywords: [replication factor, leader follower, quorum, replica lag, failure domain]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-DDS-0001]
source_ids: [SRC-000086, SRC-000087, SRC-000088]
acceptance_criteria: [Replica placement, synchronous/asynchronous behavior and lag controls are covered]
---
# Replication Models

Replication factor és placement policy határozza meg, hány failure domainben él egy adatpéldány. Synchronous acknowledgement erősebb write durability/visibility ígéretet adhat, de növeli a latency-t; asynchronous replication alacsonyabb latency mellett lagot és stale read-et engedhet.

Írd le a leader/follower vagy leaderless modellt, az acknowledgement feltételeit, a read repair/recovery mechanizmust és a replica lag SLO-ját. A node count önmagában nem bizonyítja a fault tolerance-t: a failure domain-ek és network path-ok számítanak.

## Források
- [Apache Cassandra Documentation](https://cassandra.apache.org/doc/latest/)
- [Apache Kafka Documentation](https://kafka.apache.org/documentation/)
- [etcd Documentation](https://etcd.io/docs/)
