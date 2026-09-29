---
schema_version: 1
id: DBKB-WH-0012
title: Clustering and File Layout
type: technology
primary_domain: data-warehouse
secondary_domains: [performance, storage]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [parquet, apache-spark, apache-iceberg]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-WH-0011]
related: []
aliases: [warehouse file layout]
search_keywords: [clustering, compaction, small files, row group, data skipping]
risk: caution
version_sensitive: true
review_cycle: 6m
research_packages: [RP-WH-0001]
source_ids: [SRC-000068, SRC-000073]
acceptance_criteria: [File size, clustering, compaction and pruning trade-offs are covered]
---
# Clustering and File Layout

File layout query performance-t és costot befolyásolja: small files, row group size, compression, clustering, compaction és statistics együtt. Optimize target engine/file format alapján, és verify-old actual scan bytes, latency, write amplification és maintenance cost mérésével.

## Források
- [Apache Parquet Documentation](https://parquet.apache.org/docs/)
- [Apache Iceberg Documentation](https://iceberg.apache.org/docs/latest/)
