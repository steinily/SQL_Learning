---
schema_version: 1
id: DBKB-INTG-0011
title: Error Queues and Replay
type: playbook
primary_domain: data-integration
secondary_domains: [reliability]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [apache-kafka, debezium]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-INTG-0010]
related: []
aliases: [dead letter queue]
search_keywords: [DLQ, dead letter, replay, poison message, quarantine]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-INT-0001]
source_ids: [SRC-000069, SRC-000070]
acceptance_criteria: [Quarantine, remediation, replay scope and deduplication are defined]
---
# Error Queues and Replay

Error queue/quarantine őrizze meg original payload identityt, failure reason-t, schema/versiont, source offsetot és first-seen time-ot. Replay csak remediation és bounded scope után induljon, deduplication/idempotency guarddal; DLQ growth legyen monitored és ownerhez rendelt.

## Források
- [Apache Kafka Documentation](https://kafka.apache.org/documentation/)
- [Debezium Documentation](https://debezium.io/documentation/)
