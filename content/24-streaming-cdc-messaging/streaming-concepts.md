---
schema_version: 1
id: DBKB-STREAM-0002
title: Streaming Concepts
type: concept
primary_domain: streaming
secondary_domains: [processing]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [apache-kafka, apache-flink]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-STREAM-0001]
related: []
aliases: [stream processing basics]
search_keywords: [unbounded data, event, state, offset, time]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-STREAM-0001]
source_ids: [SRC-000069, SRC-000072]
acceptance_criteria: [Unbounded input, event lifecycle, state and time concepts are explained]
---
# Streaming Concepts

Streamingben event ingestion, partitioning, processing, state update, checkpoint és sink commit folyamatosan történik. Distinguish-old event time, processing time, ingestion time, at-least-once replay és business-level deduplication fogalmait.

## Források
- [Apache Kafka Documentation](https://kafka.apache.org/documentation/)
- [Apache Flink Documentation](https://nightlies.apache.org/flink/flink-docs-stable/)
