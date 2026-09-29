---
schema_version: 1
id: DBKB-INTG-0007
title: Schema Registry and Serialization
type: technology
primary_domain: data-integration
secondary_domains: [data-contracts]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [avro, apache-kafka]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-INTG-0006]
related: []
aliases: [schema registry]
search_keywords: [schema registry, Avro, serialization, compatibility, subject]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-INT-0001]
source_ids: [SRC-000071, SRC-000069]
acceptance_criteria: [Schema identity, serialization, compatibility and rollout are defined]
---
# Schema Registry and Serialization

Schema registry producer/consumer contract versioneit és compatibility policy-ját kezeli; serialization a payload bytes representationje. Subject naming, schema ID, backward/forward/full compatibility, default/null semantics és unknown field handling implementation-specific, ezért consumer matrix és actual decode test kell.

## Források
- [Apache Avro Documentation](https://avro.apache.org/docs/)
- [Apache Kafka Documentation](https://kafka.apache.org/documentation/)
