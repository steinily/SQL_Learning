---
schema_version: 1
id: DBKB-INTG-0017
title: Integration Runbook
type: playbook
primary_domain: data-integration
secondary_domains: [operations]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [apache-kafka, debezium, avro]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-INTG-0016]
related: []
aliases: [integration operations runbook]
search_keywords: [integration runbook, pause, resume, replay, connector restart]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-INT-0001]
source_ids: [SRC-000069, SRC-000070]
acceptance_criteria: [Prechecks, pause/resume, replay, validation and escalation are specified]
---
# Integration Runbook

Runbookban source/target, topic/connector identity, schema version, ownership, precheck, pause/drain, restart, offset handling, DLQ/replay, reconciliation, security és escalation steps legyenek. Minden destructive offset vagy retention művelethez approval, backup/evidence és abort path szükséges.

## Források
- [Apache Kafka Documentation](https://kafka.apache.org/documentation/)
- [Debezium Documentation](https://debezium.io/documentation/)
