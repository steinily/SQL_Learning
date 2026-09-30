---
schema_version: 1
id: DBKB-REC-0022
title: Distributed Data Recipes
type: playbook
primary_domain: recipes
secondary_domains: [distributed-data-systems, reliability]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [apache-cassandra, apache-kafka, etcd]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-REC-0021]
related: [DBKB-DDS-0001]
aliases: [distributed database runbook]
search_keywords: [quorum, partition, replica, lag, repair, replay]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-RECIPES-0001]
source_ids: [SRC-000086, SRC-000087, SRC-000088]
acceptance_criteria: [Partitioning, quorum, retry, repair, replay and failure evidence are actionable]
---
# Distributed Data Recipes

Recipe mindig jelölje a partition/key, replica placement, consistency/ack, timeout/retry és failure domain döntést. Quorum vagy leader loss alatt ne force-write-olj unknown state-be; first capture term/offset/lag and membership evidence.

Repair/rebalance/replay legyen throttled, idempotent és resumable. Post-check: convergence, count/checksum, consumer lag, reconciliation és SLO; „job completed” nem execution proof.

## Források
- [Apache Cassandra Documentation](https://cassandra.apache.org/doc/latest/)
- [Apache Kafka Documentation](https://kafka.apache.org/documentation/)
- [etcd Documentation](https://etcd.io/docs/)
