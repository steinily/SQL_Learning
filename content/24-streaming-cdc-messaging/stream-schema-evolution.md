---
schema_version: 1
id: DBKB-STREAM-0012
title: Stream Schema Evolution
type: technology
primary_domain: streaming
secondary_domains: [data-contracts]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [apache-kafka, debezium, avro]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-STREAM-0011]
related: []
aliases: [event schema evolution]
search_keywords: [schema evolution, compatibility, default, nullable, registry]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-STREAM-0001]
source_ids: [SRC-000070, SRC-000071]
acceptance_criteria: [Compatibility policy, consumer matrix and rollout are defined]
---
# Stream Schema Evolution

Stream schema evolution backward/forward/full compatibility policy, default/null behavior, unknown field handling és consumer rollout matrix alapján történjen. CDC schema change event és registry versioning külön evidence; breaking field rename/drop előtt dual-read vagy coordinated cutover kell.

## Források
- [Debezium Documentation](https://debezium.io/documentation/)
- [Apache Avro Documentation](https://avro.apache.org/docs/)
