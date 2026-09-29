---
schema_version: 1
id: DBKB-INTG-0009
title: Deduplication and Idempotency
type: concept
primary_domain: data-integration
secondary_domains: [reliability]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [apache-kafka, debezium, apache-spark]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-INTG-0008]
related: []
aliases: [integration deduplication]
search_keywords: [deduplication, idempotent consumer, event ID, replay]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-INT-0001]
source_ids: [SRC-000069, SRC-000070]
acceptance_criteria: [Identity key, duplicate window, replay and side-effect safety are defined]
---
# Deduplication and Idempotency

Deduplication stable event/message identity, source position, duplicate window és storage/index policy alapján működik. Consumer processing legyen idempotent vagy transactional outbox/inbox patternnel védett; unbounded dedup state, late duplicate és replay behavior explicit legyen.

## Források
- [Apache Kafka Documentation](https://kafka.apache.org/documentation/)
- [Debezium Documentation](https://debezium.io/documentation/)
