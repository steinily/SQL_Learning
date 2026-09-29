---
schema_version: 1
id: DBKB-DE-0003
title: Batch and Streaming Processing
type: comparison
primary_domain: data-engineering
secondary_domains: [processing]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [apache-spark]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-DE-0002]
related: []
aliases: [batch versus streaming]
search_keywords: [batch, streaming, latency, watermark, micro-batch]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-DE-0001]
source_ids: [SRC-000066]
acceptance_criteria: [Latency, completeness, ordering and operational trade-offs are distinguished]
---
# Batch and Streaming Processing

Batch bounded inputon, streaming pedig folyamatos event/data arrivalon dolgozik; a boundary nem pusztán schedule frequency. Streamingnél ordering, late data, watermark, checkpoint és replay semantics, batchnél completeness, backfill és bounded resource window explicit legyen.

## Források
- [Apache Spark Documentation](https://spark.apache.org/docs/latest/)
