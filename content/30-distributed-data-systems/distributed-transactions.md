---
schema_version: 1
id: DBKB-DDS-0010
title: Distributed Transactions
type: technology
primary_domain: distributed-data-systems
secondary_domains: [application-design, data-integrity]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [apache-cassandra, etcd]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-DDS-0009]
related: [DBKB-TX-0001, DBKB-DDS-0011]
aliases: [distributed commit, cross-partition transaction]
search_keywords: [distributed transaction, atomicity, saga, two phase commit]
risk: production-critical
version_sensitive: true
review_cycle: 12m
research_packages: [RP-DDS-0001]
source_ids: [SRC-000086, SRC-000088]
acceptance_criteria: [Cross-partition atomicity tradeoffs and compensating patterns are distinguished]
---
# Distributed Transactions

Cross-partition atomicityt ne feltételezd abból, hogy minden node ugyanazt a replication protocolt használja. Először definiáld a business invariantet, a commit boundary-t, a retry/idempotency policy-t és a partial failure recovery-t.

Ha a rendszer nem ad natív distributed transactiont, használj explicit workflow-t, outbox/inbox mintát vagy Saga-style compensationt, és rögzítsd, mely intermediate state-ek láthatók. A compensation nem rollback: üzleti ellenművelet, saját failure path-tal.

## Források
- [Apache Cassandra Documentation](https://cassandra.apache.org/doc/latest/)
- [etcd Documentation](https://etcd.io/docs/)
