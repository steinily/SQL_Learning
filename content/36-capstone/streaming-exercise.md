---
schema_version: 1
id: DBKB-CAP-0033
title: Streaming Exercise
type: exercise
primary_domain: capstone
secondary_domains: [streaming, reliability]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [apache-kafka]
sql_dialects: []
scope: vendor-specific
prerequisites: [DBKB-CAP-0032]
related: [DBKB-STREAM-0001]
aliases: [streaming lab]
search_keywords: [Kafka exercise, partition, lag, replay, consumer group]
risk: production-critical
version_sensitive: true
review_cycle: 12m
research_packages: [RP-CAPSTONE-0001]
source_ids: [SRC-000087]
acceptance_criteria: [Learner tests partitioning, ordering, lag, replay, retention and duplicate handling]
---
# Streaming Exercise

Állíts be topic/partition/retention és consumer group scenariot, majd injectálj lagot, duplicate-ot, rebalance-t és bounded replay-t. Mérd partition skew, offset, error, retry és end-to-end freshness értékét.

Rögzítsd key strategy, ordering scope, commit policy, idempotency és reconciliation outputot. Exactly-once claim csak a ténylegesen tesztelt teljes pipeline feltételeivel adható.

## Forrás
- [Apache Kafka Documentation](https://kafka.apache.org/documentation/)
