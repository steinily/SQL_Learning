---
schema_version: 1
id: DBKB-DE-0006
title: Data Partitioning
type: technology
primary_domain: data-engineering
secondary_domains: [performance]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [apache-spark, parquet]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-DE-0003]
related: []
aliases: [data partitioning strategy]
search_keywords: [partitioning, partition pruning, skew, file layout]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-DE-0001]
source_ids: [SRC-000066, SRC-000068]
acceptance_criteria: [Partition key, pruning, skew and small-file risks are explained]
---
# Data Partitioning

Partition key-et query/selectivity, temporal access, cardinality, skew, retention és write pattern alapján válaszd. Túl sok partition metadata overheadot, túl kevés scan costot, skew pedig straggler-t okozhat; partition pruning és file layout target implementationen validálandó.

## Források
- [Apache Spark Documentation](https://spark.apache.org/docs/latest/)
- [Apache Parquet Documentation](https://parquet.apache.org/docs/)
