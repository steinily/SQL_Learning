---
schema_version: 1
id: DBKB-CAP-0010
title: Streaming Case Study
type: case-study
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
prerequisites: [DBKB-CAP-0009]
related: [DBKB-STREAM-0001]
aliases: [streaming case]
search_keywords: [Kafka, consumer lag, replay, partition, exactly once]
risk: production-critical
version_sensitive: true
review_cycle: 12m
research_packages: [RP-CAPSTONE-0001]
source_ids: [SRC-000087]
acceptance_criteria: [Scenario requires partition, ordering, lag, replay, retention and delivery decisions]
---
# Streaming Case Study

Order event streamben egy consumer group lagja nő, partition skew és duplicate delivery látható. Elemezd key/partition choice-t, ordering scope-ot, offset commitot, retentiont, retry/DLQ-t és replay safety-t.

Elvárt evidence: consumer lag timeline, partition distribution, message/offset samples, idempotency proof, reconciliation és recovery runbook. Exactly-once claim csak a teljes tested pipeline feltételeivel használható.

## Forrás
- [Apache Kafka Documentation](https://kafka.apache.org/documentation/)
