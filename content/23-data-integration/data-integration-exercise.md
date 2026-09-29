---
schema_version: 1
id: DBKB-INTG-0018
title: Data Integration Exercise
type: exercise
primary_domain: data-integration
secondary_domains: [validation]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [apache-kafka, debezium, avro, postgresql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-INTG-0017]
related: []
aliases: [integration exercise]
search_keywords: [CDC exercise, schema evolution, replay, reconciliation]
risk: caution
version_sensitive: false
review_cycle: 6m
research_packages: [RP-INT-0001]
source_ids: [SRC-000069, SRC-000070, SRC-000071]
acceptance_criteria: [Exercise defines evidence without claiming unexecuted results]
---
# Data Integration Exercise

Tervezd meg egy CDC source → Kafka → schema serialization → consumer sink flow-t schema evolution, duplicate, connector restart és DLQ replay eseménnyel. Rögzíts offsetet, event ID-t, lagot, reconciliation outputot, security evidence-et és recovery döntést; execution-verified csak tényleges futtatás után jelölhető.

## Források
- [Apache Kafka Documentation](https://kafka.apache.org/documentation/)
- [Debezium Documentation](https://debezium.io/documentation/)
- [Apache Avro Documentation](https://avro.apache.org/docs/)
