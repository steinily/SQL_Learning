---
schema_version: 1
id: DBKB-DDS-0003
title: Partitioning and Sharding
type: technology
primary_domain: distributed-data-systems
secondary_domains: [data-modeling, performance]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [apache-cassandra, apache-kafka]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-DDS-0002]
related: [DBKB-DDS-0004, DBKB-DDS-0014]
aliases: [partition key, shard key]
search_keywords: [partition key, shard key, hotspot, hash partitioning, range partitioning]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-DDS-0001]
source_ids: [SRC-000086, SRC-000087]
acceptance_criteria: [Partition-key selection, hotspots, locality and repartitioning are explained]
---
# Partitioning and Sharding

Partition key választásakor a cardinality, access pattern, data locality és expected growth együtt számít. Rossz kulcs hotspotot vagy skew-t okoz; a jó distribution nem garantálja, hogy minden query olcsó lesz.

Kerüld a kontrollálatlan unbounded partitiont, és definiáld a maximum méretet vagy time bucketet. A partition map változásakor rebalancing, dual-read, backfill és rollback terv kell. Kafka esetén a partition a parallelism és ordering scope része; Cassandra esetén a partition key a data placement alapja.

## Források
- [Apache Cassandra Documentation](https://cassandra.apache.org/doc/latest/)
- [Apache Kafka Documentation](https://kafka.apache.org/documentation/)
