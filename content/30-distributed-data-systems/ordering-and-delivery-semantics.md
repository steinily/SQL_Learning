---
schema_version: 1
id: DBKB-DDS-0012
title: Ordering and Delivery Semantics
type: technology
primary_domain: distributed-data-systems
secondary_domains: [streaming, application-design]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [apache-kafka]
sql_dialects: []
scope: vendor-specific
prerequisites: [DBKB-DDS-0011]
related: [DBKB-STREAM-0001]
aliases: [message ordering, delivery guarantee]
search_keywords: [Kafka ordering, at least once, exactly once, offset, duplicate]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-DDS-0001]
source_ids: [SRC-000087]
acceptance_criteria: [Partition-scoped ordering and delivery tradeoffs are distinguished]
---
# Ordering and Delivery Semantics

Kafka-ban az ordering scope tipikusan partition-szintű; a topic teljes globális sorrendjét ne feltételezd. A key választása ezért egyszerre határozza meg az orderinget, a load distributiont és a consumer parallelism-et.

Delivery semantics esetén különítsd el at-most-once, at-least-once és exactly-once claims-et. Consumer offset, transaction boundary, replay és deduplication legyen tesztelt; „exactly-once” csak a teljes end-to-end pipeline-ra megadott feltételekkel használható.

## Forrás
- [Apache Kafka Documentation](https://kafka.apache.org/documentation/)
