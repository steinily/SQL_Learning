---
schema_version: 1
id: DBKB-STOR-0003
title: Parquet Format
type: technology
primary_domain: data-storage
secondary_domains: [interoperability]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [parquet]
sql_dialects: [postgresql, tsql, mysql]
scope: vendor-specific
prerequisites: [DBKB-STOR-0002]
related: []
aliases: [Apache Parquet]
search_keywords: [Parquet, row group, page, encoding, compression, statistics]
risk: caution
version_sensitive: true
review_cycle: 6m
research_packages: [RP-STOR-0001]
source_ids: [SRC-000068]
acceptance_criteria: [Parquet structure, encoding, compression and compatibility are scoped]
---
# Parquet Format

Parquet file row group/page/column chunk struktúrája encoding, compression és column statistics lehetőségeket ad. Logical type, timestamp, decimal, schema evolution és reader feature support implementation/versionfüggő; producer-consumer párossal actual read/write és predicate behavior tesztelendő.

## Források
- [Apache Parquet Documentation](https://parquet.apache.org/docs/)
