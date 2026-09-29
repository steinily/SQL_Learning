---
schema_version: 1
id: DBKB-STREAM-0006
title: Windows and Watermarks
type: technology
primary_domain: streaming
secondary_domains: [processing]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [apache-flink]
sql_dialects: [postgresql, tsql, mysql]
scope: vendor-specific
prerequisites: [DBKB-STREAM-0005]
related: []
aliases: [stream windows watermarks]
search_keywords: [tumbling window, sliding window, session window, watermark, lateness]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-STREAM-0001]
source_ids: [SRC-000072]
acceptance_criteria: [Window types, watermark, lateness and state cleanup are scoped]
---
# Windows and Watermarks

Window aggregation tumbling, sliding vagy session boundaryt használ; watermark a vízjel alapján jelzi, meddig várható event-time adat. Allowed lateness, late side output, state cleanup és result update semantics target Flink versionen és sink contracton validálandó.

## Források
- [Apache Flink Documentation](https://nightlies.apache.org/flink/flink-docs-stable/)
