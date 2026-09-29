---
schema_version: 1
id: DBKB-STOR-0016
title: Storage and File Formats Exercise
type: exercise
primary_domain: data-storage
secondary_domains: [validation]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [parquet, apache-orc, avro, apache-arrow, json]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-STOR-0015]
related: []
aliases: [file format exercise]
search_keywords: [storage exercise, format conversion, schema evolution, compaction]
risk: caution
version_sensitive: false
review_cycle: 6m
research_packages: [RP-STOR-0001]
source_ids: [SRC-000068, SRC-000071, SRC-000074, SRC-000075, SRC-000076]
acceptance_criteria: [Exercise defines evidence without claiming unexecuted results]
---
# Storage and File Formats Exercise

Hasonlítsd össze ugyanazon fixture Parquet, ORC, Avro, Arrow és JSON reprezentációját: schema/precision, size, read/write, round-trip, null/missing, compression és reader compatibility. Rögzítsd target implementationt, output hash/countot, lifecycle döntést és trade-offot; execution-verified csak valódi futtatás után jelölhető.

## Források
- [Apache Parquet Documentation](https://parquet.apache.org/docs/)
- [Apache ORC Documentation](https://orc.apache.org/docs/)
- [Apache Avro Documentation](https://avro.apache.org/docs/)
- [Apache Arrow Documentation](https://arrow.apache.org/docs/)
