---
schema_version: 1
id: DBKB-DDS-0014
title: Rebalancing and Repair
type: playbook
primary_domain: distributed-data-systems
secondary_domains: [operations, availability]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [apache-cassandra, apache-kafka]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-DDS-0013]
related: [DBKB-DDS-0003, DBKB-DDS-0004]
aliases: [cluster rebalance, replica repair]
search_keywords: [rebalancing, repair, bootstrap, partition movement, throttling]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-DDS-0001]
source_ids: [SRC-000086, SRC-000087]
acceptance_criteria: [Prechecks, throttling, observability and post-repair verification are defined]
---
# Rebalancing and Repair

Rebalancing előtt inventoryzd a capacity-t, partition ownershipot, replica lagot és failure domain-t. A movement/repair legyen throttled, hogy a foreground workload és a recovery traffic együtt az SLO alatt maradjon.

Készíts prechecket, maintenance window-t, abort és rollback tervet. Utólag ellenőrizd a token/partition coverage-et, replica convergence-et, consumer lagot, error rate-et és checksum vagy count reconciliationt; a „job completed” önmagában nem bizonyítja az adat-helyességet.

## Források
- [Apache Cassandra Documentation](https://cassandra.apache.org/doc/latest/)
- [Apache Kafka Documentation](https://kafka.apache.org/documentation/)
