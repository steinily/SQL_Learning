---
schema_version: 1
id: DBKB-INTG-0008
title: Data Mapping and Transformation
type: playbook
primary_domain: data-integration
secondary_domains: [data-quality]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [apache-spark, avro]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-INTG-0007]
related: []
aliases: [integration mapping]
search_keywords: [mapping, transformation, type conversion, null semantics, lookup]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-INT-0001]
source_ids: [SRC-000066, SRC-000071]
acceptance_criteria: [Mapping specification, null/type semantics and reconciliation are covered]
---
# Data Mapping and Transformation

Mapping specification-ben source/target field, type/scale, null/default, code set, timezone, precision, lookup, error/quarantine és ownership szerepeljen. Transformation legyen deterministic és testelt; implicit cast, locale vagy truncation parity-check nélkül silent data loss-t okozhat.

## Források
- [Apache Spark Documentation](https://spark.apache.org/docs/latest/)
- [Apache Avro Documentation](https://avro.apache.org/docs/)
