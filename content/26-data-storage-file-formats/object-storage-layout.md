---
schema_version: 1
id: DBKB-STOR-0012
title: Object Storage Layout
type: technology
primary_domain: data-storage
secondary_domains: [architecture]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [parquet, apache-orc, apache-iceberg]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-STOR-0011]
related: []
aliases: [data lake object layout]
search_keywords: [object storage, prefix, partition path, manifest, atomic publish]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-STOR-0001]
source_ids: [SRC-000068, SRC-000073]
acceptance_criteria: [Path, partition, manifest, atomic publish and metadata layout are defined]
---
# Object Storage Layout

Object storage layout-ban legyen domain/table/version/partition path, manifest vagy catalog identity, atomic publish convention és orphan cleanup policy. Prefix naming nem helyettesíti a schema/catalog metadata-t; concurrent writer, partial upload és eventual listing behavior target storageban validálandó.

## Források
- [Apache Parquet Documentation](https://parquet.apache.org/docs/)
- [Apache Iceberg Documentation](https://iceberg.apache.org/docs/latest/)
