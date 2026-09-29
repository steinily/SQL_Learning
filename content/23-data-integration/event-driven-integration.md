---
schema_version: 1
id: DBKB-INTG-0005
title: Event Driven Integration
type: technology
primary_domain: data-integration
secondary_domains: [messaging]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [apache-kafka, avro]
sql_dialects: [postgresql, tsql, mysql]
scope: vendor-specific
prerequisites: [DBKB-INTG-0002]
related: []
aliases: [event-driven architecture]
search_keywords: [event, topic, partition, consumer group, offset]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-INT-0001]
source_ids: [SRC-000069, SRC-000071]
acceptance_criteria: [Topic, partition, consumer, offset and event contract semantics are explained]
---
# Event Driven Integration

Event-driven integrationben producer eventet topic/partitionon publikál, consumer group offset alapján dolgoz fel. Ordering partition-scope, replay offset/state függő, retention és delivery semantics konfiguráció/client dependent; event schema, key, correlation ID és error path legyen contract része.

## Források
- [Apache Kafka Documentation](https://kafka.apache.org/documentation/)
- [Apache Avro Documentation](https://avro.apache.org/docs/)
