---
schema_version: 1
id: DBKB-DDS-0002
title: Distribution Models
type: concept
primary_domain: distributed-data-systems
secondary_domains: [architecture]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [apache-cassandra, apache-kafka, etcd]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-DDS-0001]
related: [DBKB-DDS-0003]
aliases: [shared-nothing, distributed topology]
search_keywords: [shared nothing, sharding, replication, coordinator, topology]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-DDS-0001]
source_ids: [SRC-000086, SRC-000087, SRC-000088]
acceptance_criteria: [Shared-nothing, partitioned and replicated distribution models are distinguished]
---
# Distribution Models

Shared-nothing modellben a node-ok saját storage és compute erőforrással rendelkeznek; a data partitioning határozza meg, melyik node kezeli a rekordot. Egy coordinator vagy client routing döntheti el, hová menjen a request.

A replication nem ugyanaz, mint a partitioning: előbbi több példányt tart fenn, utóbbi a key space-t osztja fel. Dokumentáld a topology-t, failure domain mappinget, placement policy-t és a rebalancing eljárást.

## Források
- [Apache Cassandra Documentation](https://cassandra.apache.org/doc/latest/)
- [Apache Kafka Documentation](https://kafka.apache.org/documentation/)
- [etcd Documentation](https://etcd.io/docs/)
