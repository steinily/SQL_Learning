---
schema_version: 1
id: DBKB-WH-0020
title: Warehouse Security
type: technology
primary_domain: data-warehouse
secondary_domains: [security-privacy]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [apache-spark, apache-iceberg, parquet]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-WH-0019]
related: []
aliases: [analytical data security]
search_keywords: [warehouse access, row-level security, masking, encryption, object storage]
risk: security-sensitive
version_sensitive: true
review_cycle: 6m
research_packages: [RP-WH-0001]
source_ids: [SRC-000066, SRC-000073]
acceptance_criteria: [Identity, access, encryption, masking and export controls are covered]
---
# Warehouse Security

Warehouse security rétegeli identity, catalog/table/column access, row-level policy, masking/tokenization, encryption, object storage permission, export és audit log alapján. Analytical extract, temporary file, cache és snapshot ugyanúgy sensitive copy, mint a primary table.

## Források
- [Apache Spark Documentation](https://spark.apache.org/docs/latest/)
- [Apache Iceberg Documentation](https://iceberg.apache.org/docs/latest/)
