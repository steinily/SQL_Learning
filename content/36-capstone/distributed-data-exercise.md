---
schema_version: 1
id: DBKB-CAP-0041
title: Distributed Data Exercise
type: exercise
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
prerequisites: [DBKB-CAP-0040]
related: [DBKB-DDS-0001]
aliases: [distributed lab]
search_keywords: [distributed exercise, partition, quorum, repair, replay]
risk: production-critical
version_sensitive: true
review_cycle: 12m
research_packages: [RP-CAPSTONE-0001]
source_ids: [SRC-000086, SRC-000087, SRC-000088]
acceptance_criteria: [Learner designs topology, consistency, failure injection, repair and recovery evidence]
---
# Distributed Data Exercise

Tervezd meg three-failure-domain event/data platform topologyját partition key, replica placement, quorum/consistency, leader coordination és client retry policy-val.

Injectálj node loss, network partition, hot partition és leader change esetet; mérd lag, offset/term, retry és reconciliation eredményt. Recovery claim csak actual run outputtal.

## Források
- [Apache Cassandra Documentation](https://cassandra.apache.org/doc/latest/)
- [Apache Kafka Documentation](https://kafka.apache.org/documentation/)
- [etcd Documentation](https://etcd.io/docs/)
