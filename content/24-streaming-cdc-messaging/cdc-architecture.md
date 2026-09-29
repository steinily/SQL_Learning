---
schema_version: 1
id: DBKB-STREAM-0010
title: CDC Architecture
type: technology
primary_domain: streaming
secondary_domains: [data-integration]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [debezium, apache-kafka, postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-STREAM-0009]
related: []
aliases: [change data capture architecture]
search_keywords: [CDC, transaction log, connector, snapshot, offset]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-STREAM-0001]
source_ids: [SRC-000070, SRC-000069]
acceptance_criteria: [Source log, connector, topic, offset, schema and sink flow are described]
---
# CDC Architecture

CDC architecture source transaction/log capture → connector state/offset → broker topic → consumer transform → sink apply láncot alkot. Snapshot-to-stream handoff, transaction boundaries, delete/tombstone, schema change, restart és duplicate/replay semantics source/connector/version függők.

## Források
- [Debezium Documentation](https://debezium.io/documentation/)
- [Apache Kafka Documentation](https://kafka.apache.org/documentation/)
