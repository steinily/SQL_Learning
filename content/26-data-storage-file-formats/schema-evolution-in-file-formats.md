---
schema_version: 1
id: DBKB-STOR-0010
title: Schema Evolution in File Formats
type: playbook
primary_domain: data-storage
secondary_domains: [data-contracts]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [parquet, apache-orc, avro, json]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-STOR-0009]
related: []
aliases: [file schema evolution]
search_keywords: [schema evolution, add column, rename, type change, compatibility]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-STOR-0001]
source_ids: [SRC-000068, SRC-000071, SRC-000074, SRC-000076]
acceptance_criteria: [Compatible changes, readers, defaults and migration evidence are defined]
---
# Schema Evolution in File Formats

File schema evolutionnél add/remove/rename/type/nullability change compatibility reader behavior, default, missing field, unknown field és mixed-version file set alapján vizsgálandó. Registry/catalog policy, producer-consumer matrix és representative old/new files testje nélkül a change nem bizonyítottan safe.

## Források
- [Apache Parquet Documentation](https://parquet.apache.org/docs/)
- [Apache Avro Documentation](https://avro.apache.org/docs/)
- [Apache ORC Documentation](https://orc.apache.org/docs/)
