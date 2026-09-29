---
schema_version: 1
id: DBKB-DE-0010
title: Columnar Storage
type: technology
primary_domain: data-engineering
secondary_domains: [performance, storage]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [parquet, apache-spark]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-DE-0009]
related: []
aliases: [columnar data format]
search_keywords: [columnar, row group, compression, projection, scan]
risk: caution
version_sensitive: true
review_cycle: 6m
research_packages: [RP-DE-0001]
source_ids: [SRC-000068]
acceptance_criteria: [Columnar access, compression and workload trade-offs are described]
---
# Columnar Storage

Columnar storage egyes oszlopok együtt tárolásával segítheti a projectiont, compressiont és analytical scan-t, miközben point lookup, frequent row mutation vagy small-file workload más trade-offot ad. File size, row group, encoding és predicate pushdown target engine-ben mérendő.

## Források
- [Apache Parquet Documentation](https://parquet.apache.org/docs/)
