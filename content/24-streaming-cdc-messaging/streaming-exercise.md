---
schema_version: 1
id: DBKB-STREAM-0020
title: Streaming Exercise
type: exercise
primary_domain: streaming
secondary_domains: [validation]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [apache-kafka, apache-flink, debezium]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-STREAM-0019]
related: []
aliases: [streaming exercise]
search_keywords: [stream exercise, CDC, watermark, replay, checkpoint]
risk: caution
version_sensitive: false
review_cycle: 6m
research_packages: [RP-STREAM-0001]
source_ids: [SRC-000069, SRC-000070, SRC-000072]
acceptance_criteria: [Exercise defines evidence without claiming unexecuted results]
---
# Streaming Exercise

Tervezd meg CDC → Kafka → stateful stream → sink flow gyakorlatát late event, duplicate, schema change, checkpoint failure és replay eseménnyel. Rögzíts offsetet, watermarkot, state/checkpoint evidence-et, lagot, reconciliationt és security/incident döntést; execution-verified csak valódi futtatás után használható.

## Források
- [Apache Kafka Documentation](https://kafka.apache.org/documentation/)
- [Apache Flink Documentation](https://nightlies.apache.org/flink/flink-docs-stable/)
- [Debezium Documentation](https://debezium.io/documentation/)
