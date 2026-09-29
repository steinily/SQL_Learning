---
schema_version: 1
id: DBKB-WH-0006
title: Surrogate Keys and Business Keys
type: concept
primary_domain: data-warehouse
secondary_domains: [data-modeling]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [apache-spark, parquet]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-WH-0005]
related: []
aliases: [warehouse key design]
search_keywords: [surrogate key, business key, natural key, key mapping]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-WH-0001]
source_ids: [SRC-000066]
acceptance_criteria: [Business/surrogate key roles, mapping and unknown handling are defined]
---
# Surrogate Keys and Business Keys

Business/natural key source identityt, surrogate key warehouse history/version identityt stabilizálhatja. Mapping table, unknown/default member, source key reuse, collision és late-arriving dimension policy legyen explicit; surrogate key önmagában nem deduplication proof.

## Források
- [Apache Spark Documentation](https://spark.apache.org/docs/latest/)
