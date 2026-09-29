---
schema_version: 1
id: DBKB-STREAM-0015
title: Stream Replay and Recovery
type: playbook
primary_domain: streaming
secondary_domains: [reliability]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [apache-kafka, apache-flink, debezium]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-STREAM-0014]
related: []
aliases: [stream recovery replay]
search_keywords: [replay, offset reset, checkpoint restore, recovery, deduplication]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-STREAM-0001]
source_ids: [SRC-000069, SRC-000070, SRC-000072]
acceptance_criteria: [Replay scope, offset/checkpoint selection, dedup and reconciliation are defined]
---
# Stream Replay and Recovery

Replay előtt scope-old partition/offset vagy event-time tartományt, checkpoint/savepointet, sink idempotency-t és downstream side-effectet. Recovery során preserve-eld original evidence-et, boundedold replay-et, monitorozd lagot és reconciliationt, és offset resetet csak approval + rollback/recovery plan mellett hajts végre.

## Források
- [Apache Kafka Documentation](https://kafka.apache.org/documentation/)
- [Apache Flink Documentation](https://nightlies.apache.org/flink/flink-docs-stable/)
- [Debezium Documentation](https://debezium.io/documentation/)
