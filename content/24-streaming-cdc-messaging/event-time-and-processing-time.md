---
schema_version: 1
id: DBKB-STREAM-0005
title: Event Time and Processing Time
type: concept
primary_domain: streaming
secondary_domains: [processing]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [apache-flink, apache-kafka]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-STREAM-0002]
related: []
aliases: [event time semantics]
search_keywords: [event time, processing time, ingestion time, late event, watermark]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-STREAM-0001]
source_ids: [SRC-000072]
acceptance_criteria: [Time domains, late data and watermark interaction are explained]
---
# Event Time and Processing Time

Event time a domain event timestampja, processing time a worker execution clockja; ingestion time a system arrival marker. Out-of-order event és clock skew miatt event-time window és watermark kell, de lateness policy nélkül a completeness és latency trade-off implicit marad.

## Források
- [Apache Flink Documentation](https://nightlies.apache.org/flink/flink-docs-stable/)
