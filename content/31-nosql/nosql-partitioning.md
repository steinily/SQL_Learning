---
schema_version: 1
id: DBKB-NOSQL-0012
title: NoSQL Partitioning
type: technology
primary_domain: nosql
secondary_domains: [distributed-data-systems, performance]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [mongodb, apache-cassandra, redis]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-NOSQL-0011]
related: [DBKB-DDS-0003]
aliases: [shard key, partition key]
search_keywords: [NoSQL sharding, shard key, partition key, hotspot, rebalance]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-NOSQL-0001]
source_ids: [SRC-000086, SRC-000089, SRC-000090]
acceptance_criteria: [Key selection, hotspot avoidance, routing and rebalancing are addressed]
---
# NoSQL Partitioning

Partition/shard key választása egyszerre határozza meg a data distributiont, query routingot, hotspotot és rebalancing costot. Mérd a cardinality-t, skew-t, tenant isolationt és a legnagyobb partition várható méretét.

Használj bounded time bucketet vagy hash prefixet, ha az access pattern megengedi, de dokumentáld a fan-out read és ordering hatását. Shard key change általában migration; előre készíts dual-read, backfill, cutover és rollback tervet.

## Források
- [MongoDB Manual](https://www.mongodb.com/docs/manual/)
- [Apache Cassandra Documentation](https://cassandra.apache.org/doc/latest/)
- [Redis Documentation](https://redis.io/docs/latest/)
