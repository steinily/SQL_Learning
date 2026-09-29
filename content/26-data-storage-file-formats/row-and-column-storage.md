---
schema_version: 1
id: DBKB-STOR-0002
title: Row and Column Storage
type: comparison
primary_domain: data-storage
secondary_domains: [performance]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [parquet, apache-orc, apache-arrow]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-STOR-0001]
related: []
aliases: [row versus columnar storage]
search_keywords: [row store, column store, scan, point lookup, compression]
risk: caution
version_sensitive: false
review_cycle: 6m
research_packages: [RP-STOR-0001]
source_ids: [SRC-000068, SRC-000074]
acceptance_criteria: [Row/column trade-offs by workload are distinguished]
---
# Row and Column Storage

Row storage adjacent record accessra és frequent row mutationre, columnar storage selected columns analytical scanjára és compressionre lehet előnyös. Workload, projection, point lookup, update pattern, file size és reader support alapján mérj; format labelből ne következtess automatikusan latency-re.

## Források
- [Apache Parquet Documentation](https://parquet.apache.org/docs/)
- [Apache ORC Documentation](https://orc.apache.org/docs/)
