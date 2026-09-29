---
schema_version: 1
id: DBKB-STREAM-0014
title: Backpressure and Flow Control
type: concept
primary_domain: streaming
secondary_domains: [reliability, performance]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [apache-flink, apache-kafka]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-STREAM-0013]
related: []
aliases: [stream backpressure]
search_keywords: [backpressure, flow control, lag, throughput, buffer]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-STREAM-0001]
source_ids: [SRC-000072, SRC-000069]
acceptance_criteria: [Producer throttling, lag, buffers and downstream capacity are described]
---
# Backpressure and Flow Control

Backpressure a downstream processing/sink capacityhoz igazítja source intake-et, buffer és queue growth-t. Monitorozd lagot, busy/backpressured time-ot, checkpoint durationt, buffer saturationt és producer throttlingot; uncontrolled buffering csak késlelteti a failure-t és adatvesztési kockázatot növel.

## Források
- [Apache Flink Documentation](https://nightlies.apache.org/flink/flink-docs-stable/)
- [Apache Kafka Documentation](https://kafka.apache.org/documentation/)
