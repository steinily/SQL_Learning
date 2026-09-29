---
schema_version: 1
id: DBKB-STOR-0011
title: Small Files and Compaction
type: playbook
primary_domain: data-storage
secondary_domains: [performance, operations]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [parquet, apache-orc, apache-iceberg]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-STOR-0010]
related: []
aliases: [small file problem]
search_keywords: [small files, compaction, file count, metadata overhead, rewrite]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-STOR-0001]
source_ids: [SRC-000068, SRC-000073]
acceptance_criteria: [Small-file impact, compaction safety and metrics are described]
---
# Small Files and Compaction

Small-file proliferation metadata/listing overheadot, task scheduling és open costot növel, compaction pedig rewrite, lock, storage és snapshot retention impactot hoz. Compaction policy-ben target file size, partition scope, concurrent writer, atomic publish, failure recovery és before/after scan metrics legyen.

## Források
- [Apache Parquet Documentation](https://parquet.apache.org/docs/)
- [Apache Iceberg Documentation](https://iceberg.apache.org/docs/latest/)
