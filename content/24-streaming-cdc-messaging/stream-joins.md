---
schema_version: 1
id: DBKB-STREAM-0013
title: Stream Joins
type: technology
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
prerequisites: [DBKB-STREAM-0006]
related: []
aliases: [stream-stream join]
search_keywords: [stream join, interval join, temporal join, state, watermark]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-STREAM-0001]
source_ids: [SRC-000072]
acceptance_criteria: [Join time bounds, state, late data and retention are explained]
---
# Stream Joins

Stream-stream, stream-table és temporal join state-et és time boundaryt igényel; join state growth, watermark, late event, missing side és retention policy explicit legyen. Unbounded join vagy skew uncontrolled memory pressure-t és non-deterministic completiont okozhat.

## Források
- [Apache Flink Documentation](https://nightlies.apache.org/flink/flink-docs-stable/)
