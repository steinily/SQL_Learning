---
schema_version: 1
id: DBKB-INTG-0002
title: Integration Patterns
type: comparison
primary_domain: data-integration
secondary_domains: [architecture]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [apache-kafka, debezium, avro]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-INTG-0001]
related: []
aliases: [integration architecture patterns]
search_keywords: [request response, batch, event, CDC, pub sub]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-INT-0001]
source_ids: [SRC-000069, SRC-000070]
acceptance_criteria: [Pattern selection trade-offs and failure modes are distinguished]
---
# Integration Patterns

Request/response, batch file, event-driven pub/sub és CDC más latency, coupling, replay, ordering és failure semantics-t ad. Pattern választásnál source capability, consumer count, consistency, operational ownership, backpressure és recovery evidence legyen explicit.

## Források
- [Apache Kafka Documentation](https://kafka.apache.org/documentation/)
- [Debezium Documentation](https://debezium.io/documentation/)
