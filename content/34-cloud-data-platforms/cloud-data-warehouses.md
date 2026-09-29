---
schema_version: 1
id: DBKB-CLOUD-0004
title: Cloud Data Warehouses
type: technology
primary_domain: cloud-data-platforms
secondary_domains: [data-warehousing, performance]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [google-bigquery, snowflake]
sql_dialects: []
scope: vendor-specific
prerequisites: [DBKB-CLOUD-0003]
related: [DBKB-WH-0001]
aliases: [cloud warehouse]
search_keywords: [BigQuery, Snowflake, warehouse, partitioning, clustering, virtual warehouse]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-CLOUD-0001]
source_ids: [SRC-000099, SRC-000100]
acceptance_criteria: [Warehouse storage, compute, partitioning/clustering, governance and workload controls are described]
---
# Cloud Data Warehouses

Cloud warehouse-ben a table design, partitioning/clustering, statistics, workload isolation és concurrency együtt határozza meg a cost/latency-t. BigQuery és Snowflake külön billing, reservation/warehouse és governance semantics-et használ.

Query patternhez igazítsd a partitiont, kerüld a full scan-t, és validáld explain/profile outputtal. Resource monitor, quota, timeout, cache policy, access role és data retention legyen production contract része; feature name alapján ne állíts vendor parityt.

## Források
- [Google Cloud BigQuery Documentation](https://cloud.google.com/bigquery/docs)
- [Snowflake Documentation](https://docs.snowflake.com/)
