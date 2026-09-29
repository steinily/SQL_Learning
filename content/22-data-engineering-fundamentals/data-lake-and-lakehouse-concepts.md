---
schema_version: 1
id: DBKB-DE-0009
title: Data Lake and Lakehouse Concepts
type: concept
primary_domain: data-engineering
secondary_domains: [architecture, storage]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [apache-spark, parquet]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-DE-0008]
related: []
aliases: [lakehouse architecture]
search_keywords: [data lake, lakehouse, raw zone, curated zone, table format]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-DE-0001]
source_ids: [SRC-000066, SRC-000068]
acceptance_criteria: [Lake/lakehouse layers, governance and consistency trade-offs are explained]
---
# Data Lake and Lakehouse Concepts

Data lake raw és semi-structured data tárolását, lakehouse pedig table/transaction/governance-szerű használatot is céloz object storage-on. A layer naming nem garantál atomicity, schema evolution vagy isolation képességet; target format, catalog és processing engine alapján kell validálni.

## Források
- [Apache Spark Documentation](https://spark.apache.org/docs/latest/)
- [Apache Parquet Documentation](https://parquet.apache.org/docs/)
