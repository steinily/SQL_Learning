---
schema_version: 1
id: DBKB-CAP-0081
title: Learning Path Distributed Systems
type: learning-path
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
prerequisites: [DBKB-CAP-0080]
related: [DBKB-CAP-0041, DBKB-CAP-0064]
aliases: [distributed systems path]
search_keywords: [distributed learning path, partition, replication, quorum, failure]
risk: production-critical
version_sensitive: true
review_cycle: 12m
research_packages: [RP-CAPSTONE-0001]
source_ids: [SRC-000086, SRC-000087, SRC-000088]
acceptance_criteria: [Ordered distributed systems path with topology, consistency, failure and recovery milestones]
---
# Learning Path Distributed Systems

Sorrend: distribution/partition → replication/consistency → quorum/consensus → idempotency/order → repair/rebalance → failure injection/recovery → distributed case/exercise/reference.

Exit criteria: topology-aware SLO, failure evidence, bounded replay/repair, reconciliation, RPO/RTO és explicit trade-off.

## Források
- [Apache Cassandra Documentation](https://cassandra.apache.org/doc/latest/)
- [Apache Kafka Documentation](https://kafka.apache.org/documentation/)
- [etcd Documentation](https://etcd.io/docs/)
