---
schema_version: 1
id: DBKB-CAP-0059
title: Reference Streaming
type: reference
primary_domain: capstone
secondary_domains: [streaming, reliability]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [apache-kafka]
sql_dialects: []
scope: vendor-specific
prerequisites: [DBKB-CAP-0058]
related: [DBKB-STREAM-0001]
aliases: [streaming checklist]
search_keywords: [streaming reference, topic, partition, offset, lag, replay]
risk: production-critical
version_sensitive: true
review_cycle: 12m
research_packages: [RP-CAPSTONE-0001]
source_ids: [SRC-000087]
acceptance_criteria: [Topic/partition, ordering, delivery, retention, lag and recovery checklist is provided]
---
# Reference Streaming

Checklist: topic/key/partition; replication/acks; ordering scope; retention; consumer group/offset; delivery semantics; schema/contract; lag; retry/DLQ; replay/idempotency; security; cost; observability; reconciliation.

Exactly-once or ordering claim legyen scope- és end-to-end conditionökkel alátámasztva, ne marketing labelként.

## Forrás
- [Apache Kafka Documentation](https://kafka.apache.org/documentation/)
