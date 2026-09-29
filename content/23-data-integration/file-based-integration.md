---
schema_version: 1
id: DBKB-INTG-0004
title: File Based Integration
type: technology
primary_domain: data-integration
secondary_domains: [storage]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [parquet, avro]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-INTG-0002]
related: []
aliases: [file exchange integration]
search_keywords: [file integration, manifest, checksum, atomic publish, schema]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-INT-0001]
source_ids: [SRC-000071]
acceptance_criteria: [File naming, manifest, checksum, atomicity and replay are defined]
---
# File Based Integration

File exchangehez immutable object/version, manifest, schema, checksum, encryption, atomic publish marker, arrival completeness és retention kell. Consumer csak verified manifest után olvasson; partial upload, duplicate file, late arrival és replay kezelése explicit legyen.

## Források
- [Apache Avro Documentation](https://avro.apache.org/docs/)
