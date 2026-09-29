---
schema_version: 1
id: DBKB-INTG-0015
title: Integration Testing
type: playbook
primary_domain: data-integration
secondary_domains: [testing-validation]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [apache-kafka, debezium, avro]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-INTG-0014]
related: []
aliases: [data integration tests]
search_keywords: [integration test, schema compatibility, replay, failure injection]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-INT-0001]
source_ids: [SRC-000069, SRC-000070, SRC-000071]
acceptance_criteria: [Contract, delivery, replay, security and reconciliation tests are specified]
---
# Integration Testing

Integration testben schema compatibility, serialization/deserialization, partition/order, duplicate/replay, connector restart, DLQ, auth failure, backpressure és source-target reconciliation szerepeljen. Test fixture és topic/offset isolation nélkül a result nem reprodukálható.

## Források
- [Apache Kafka Documentation](https://kafka.apache.org/documentation/)
- [Debezium Documentation](https://debezium.io/documentation/)
- [Apache Avro Documentation](https://avro.apache.org/docs/)
