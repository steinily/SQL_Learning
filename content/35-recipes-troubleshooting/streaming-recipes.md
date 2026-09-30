---
schema_version: 1
id: DBKB-REC-0018
title: Streaming Recipes
type: playbook
primary_domain: recipes
secondary_domains: [streaming, reliability]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [apache-kafka]
sql_dialects: []
scope: vendor-specific
prerequisites: [DBKB-REC-0017]
related: [DBKB-STREAM-0001]
aliases: [Kafka recipe]
search_keywords: [Kafka, topic, partition, consumer group, offset, replay]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-RECIPES-0001]
source_ids: [SRC-000087]
acceptance_criteria: [Topic/partition, offset, ordering, replay, consumer lag and delivery controls are covered]
---
# Streaming Recipes

Topic recipeben rögzítsd a key/partition strategy-t, ordering scope-ot, retentiont, replicationt, producer acks-et, consumer groupot és offset commit policy-t. Schema evolution és CloudEvents/AsyncAPI contract legyen publish gate.

Consumer lag, rebalance, duplicate, poison message és dead-letter queue monitorozandó. Replay előtt állítsd meg vagy izoláld a consumer pathot, válassz idempotency/deduplication stratégiát, és reconciliation outputtal zárd a futást.

## Forrás
- [Apache Kafka Documentation](https://kafka.apache.org/documentation/)
