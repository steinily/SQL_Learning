---
schema_version: 1
id: DBKB-CAP-0064
title: Reference Distributed Data
type: reference
primary_domain: capstone
secondary_domains: [distributed-data-systems, reliability]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [apache-cassandra, apache-kafka, etcd]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-CAP-0063]
related: [DBKB-DDS-0001]
aliases: [distributed checklist]
search_keywords: [distributed reference, partition, replication, quorum, lag, repair]
risk: production-critical
version_sensitive: true
review_cycle: 12m
research_packages: [RP-CAPSTONE-0001]
source_ids: [SRC-000086, SRC-000087, SRC-000088]
acceptance_criteria: [Topology, partition, consistency, failure, repair and recovery checklist is provided]
---
# Reference Distributed Data

Checklist: partition/shard; replica placement/failure domain; consistency/ack; leader/quorum; latency; retry/idempotency; ordering; lag; repair/rebalance; replay; security; backup; RPO/RTO; reconciliation.

Node count vagy job completion nem bizonyít fault tolerance/correctness; topology-aware failure test és post-recovery validation kell.

## Források
- [Apache Cassandra Documentation](https://cassandra.apache.org/doc/latest/)
- [Apache Kafka Documentation](https://kafka.apache.org/documentation/)
- [etcd Documentation](https://etcd.io/docs/)
