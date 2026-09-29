---
schema_version: 1
id: DBKB-WH-0022
title: Warehouse Exercise
type: exercise
primary_domain: data-warehouse
secondary_domains: [validation]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [apache-spark, parquet, apache-iceberg]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-WH-0021]
related: []
aliases: [warehouse exercise]
search_keywords: [warehouse exercise, dimensional model, SCD, metric, reconciliation]
risk: caution
version_sensitive: false
review_cycle: 6m
research_packages: [RP-WH-0001]
source_ids: [SRC-000066, SRC-000068, SRC-000073]
acceptance_criteria: [Exercise defines evidence without claiming unexecuted results]
---
# Warehouse Exercise

Tervezd meg egy dimensional warehouse-t SCD Type 2 dimensionnel, incremental fact load-dal, Parquet/Iceberg storage-gel, semantic metric layerrel és BI serving modellel. Rögzíts grain, keys, partitions, quality/reconciliation, access és query evidence-et; execution-verified csak valódi futtatás után adható.

## Források
- [Apache Spark Documentation](https://spark.apache.org/docs/latest/)
- [Apache Parquet Documentation](https://parquet.apache.org/docs/)
- [Apache Iceberg Documentation](https://iceberg.apache.org/docs/latest/)
