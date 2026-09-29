---
schema_version: 1
id: DBKB-STREAM-0009
title: Delivery Guarantees
type: concept
primary_domain: streaming
secondary_domains: [reliability]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [apache-kafka, apache-flink]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-STREAM-0008]
related: []
aliases: [stream delivery semantics]
search_keywords: [at most once, at least once, exactly once, transactional sink]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-STREAM-0001]
source_ids: [SRC-000069, SRC-000072]
acceptance_criteria: [End-to-end delivery semantics and boundary caveats are explicit]
---
# Delivery Guarantees

At-most-once veszteséget, at-least-once duplikációt, exactly-once pedig csak teljes source→state→sink transaction boundaryn belüli dedup/commit semantics-t céloz. Kafka producer, Flink checkpoint, connector és external sink külön guarantee-jeit ne add össze automatikusan.

## Források
- [Apache Kafka Documentation](https://kafka.apache.org/documentation/)
- [Apache Flink Documentation](https://nightlies.apache.org/flink/flink-docs-stable/)
