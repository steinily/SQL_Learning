---
schema_version: 1
id: DBKB-STREAM-0001
title: Streaming CDC and Messaging Overview
type: overview
primary_domain: streaming
secondary_domains: [messaging, data-integration]
levels: [beginner]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [apache-kafka, debezium, apache-flink]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-INTG-0001]
related: []
aliases: [streaming overview]
search_keywords: [streaming, CDC, messaging, event, state, offset]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-STREAM-0001]
source_ids: [SRC-000069, SRC-000070, SRC-000072]
acceptance_criteria: [Streaming scope, state, delivery and recovery semantics are defined]
---
# Streaming CDC and Messaging Overview

Streaming rendszer unbounded event flow-t dolgoz fel, CDC pedig database changes-ből eventeket képez. Topic/partition, offset, event time, watermark, state, checkpoint, schema, delivery guarantee és sink side-effect együtt adja az end-to-end semantics-t.

## Források
- [Apache Kafka Documentation](https://kafka.apache.org/documentation/)
- [Debezium Documentation](https://debezium.io/documentation/)
- [Apache Flink Documentation](https://nightlies.apache.org/flink/flink-docs-stable/)
