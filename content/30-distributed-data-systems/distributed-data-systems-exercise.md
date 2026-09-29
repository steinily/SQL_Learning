---
schema_version: 1
id: DBKB-DDS-0020
title: Distributed Data Systems Exercise
type: exercise
primary_domain: distributed-data-systems
secondary_domains: [architecture, operations]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [apache-cassandra, apache-kafka, etcd]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-DDS-0019]
related: [DBKB-DDS-0011, DBKB-DDS-0015]
aliases: [distributed systems lab]
search_keywords: [distributed systems exercise, failure injection, quorum, replay]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-DDS-0001]
source_ids: [SRC-000086, SRC-000087, SRC-000088]
acceptance_criteria: [Learner produces topology, consistency, failure test and operations evidence]
---
# Distributed Data Systems Exercise

Tervezd meg egy három failure domaines event/data platformot, amelynek van durable logja, replicated operational store-ja és consistent coordination service-e.

1. Válaszd ki a partition key-t, replication placementet és operation-level consistency-t.
2. Írd le a retry/idempotency, ordering, lag és reconciliation contractot.
3. Tervezz failure injectiont: node loss, network partition, hot partition, leader change és region outage.
4. Adj meg SLO-kat, RPO/RTO-t, alertokat, rollbacket és audit evidence-et.

Elvárt eredmény: architecture decision record, topology diagram, failure matrix, runbook és post-test report. Benchmark vagy execution-verified állítás csak tényleges futtatási outputtal fogadható el.

## Források
- [Apache Cassandra Documentation](https://cassandra.apache.org/doc/latest/)
- [Apache Kafka Documentation](https://kafka.apache.org/documentation/)
- [etcd Documentation](https://etcd.io/docs/)
