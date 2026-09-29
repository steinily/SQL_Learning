---
schema_version: 1
id: DBKB-STOR-0004
title: Avro Format
type: technology
primary_domain: data-storage
secondary_domains: [data-integration]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [avro]
sql_dialects: [postgresql, tsql, mysql]
scope: vendor-specific
prerequisites: [DBKB-STOR-0001]
related: []
aliases: [Apache Avro]
search_keywords: [Avro, schema resolution, serialization, binary encoding]
risk: caution
version_sensitive: true
review_cycle: 6m
research_packages: [RP-STOR-0001]
source_ids: [SRC-000071]
acceptance_criteria: [Avro schema, encoding, resolution and evolution are explained]
---
# Avro Format

Avro schema-based serializationt és schema resolutiont ad, különösen event/integration payloadoknál hasznos. Writer/reader schema compatibility, defaults, union/null, logical types és implementation version alapján kell tesztelni; schema registry policy külön governance layer.

## Források
- [Apache Avro Documentation](https://avro.apache.org/docs/)
