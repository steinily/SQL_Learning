---
schema_version: 1
id: DBKB-INTG-0016
title: Integration Troubleshooting
type: troubleshooting
primary_domain: data-integration
secondary_domains: [operations]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [apache-kafka, debezium, avro]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-INTG-0015]
related: []
aliases: [integration failure diagnosis]
search_keywords: [consumer lag, connector failure, schema error, DLQ, offset]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-INT-0001]
source_ids: [SRC-000069, SRC-000070, SRC-000071]
acceptance_criteria: [Failure classification, offset safety and replay discipline are defined]
---
# Integration Troubleshooting

Hiba lehet producer, broker/topic, partition, consumer, connector/source DB, schema registry, auth/network, transform vagy downstream sink oldalon. Preserve-eld offset/partition/event ID/task state-et; blind offset reset, uncontrolled replay vagy DLQ purge adatvesztést és duplikációt okozhat.

## Források
- [Apache Kafka Documentation](https://kafka.apache.org/documentation/)
- [Debezium Documentation](https://debezium.io/documentation/)
