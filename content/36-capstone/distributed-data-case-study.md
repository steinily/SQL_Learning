---
schema_version: 1
id: DBKB-CAP-0018
title: Distributed Data Case Study
type: case-study
primary_domain: capstone
secondary_domains: [distributed-data-systems, reliability]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [apache-cassandra, apache-kafka, etcd]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-CAP-0017]
related: [DBKB-DDS-0001]
aliases: [distributed case]
search_keywords: [partition, replication, quorum, leader, failure, repair]
risk: production-critical
version_sensitive: true
review_cycle: 12m
research_packages: [RP-CAPSTONE-0001]
source_ids: [SRC-000086, SRC-000087, SRC-000088]
acceptance_criteria: [Scenario requires topology, consistency, partition, repair, replay and recovery evidence]
---
# Distributed Data Case Study

Három regionben futó event/data platform network partition, hot partition és leader loss eseményt tapasztal. Tervezz placement, quorum/consistency, fencing, retry, repair, replay és failover decision tree-t.

Elvárt evidence: topology, lag/term/offset, partition skew, failure injection, reconciliation, RPO/RTO és post-recovery validation. Benchmarkot és production claimet csak tényleges outputtal jelölj.

## Források
- [Apache Cassandra Documentation](https://cassandra.apache.org/doc/latest/)
- [Apache Kafka Documentation](https://kafka.apache.org/documentation/)
- [etcd Documentation](https://etcd.io/docs/)
