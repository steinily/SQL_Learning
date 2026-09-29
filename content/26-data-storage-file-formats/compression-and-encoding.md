---
schema_version: 1
id: DBKB-STOR-0009
title: Compression and Encoding
type: concept
primary_domain: data-storage
secondary_domains: [performance, cost]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [parquet, apache-orc, avro]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-STOR-0003]
related: []
aliases: [file compression encoding]
search_keywords: [compression codec, encoding, dictionary, run length, trade-off]
risk: caution
version_sensitive: true
review_cycle: 6m
research_packages: [RP-STOR-0001]
source_ids: [SRC-000068, SRC-000071, SRC-000074]
acceptance_criteria: [Encoding/codec choice, read/write CPU and compatibility are explained]
---
# Compression and Encoding

Encoding value representationt, compression pedig byte volume-t csökkent; dictionary, run-length, delta és codec választás data distribution, CPU, scan, random access és compatibility trade-off. Measure file size, write/read CPU, scan throughput, decompression support és downstream interoperability target stacken.

## Források
- [Apache Parquet Documentation](https://parquet.apache.org/docs/)
- [Apache ORC Documentation](https://orc.apache.org/docs/)
- [Apache Avro Documentation](https://avro.apache.org/docs/)
