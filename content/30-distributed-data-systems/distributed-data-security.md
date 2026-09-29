---
schema_version: 1
id: DBKB-DDS-0018
title: Distributed Data Security
type: technology
primary_domain: distributed-data-systems
secondary_domains: [security, operations]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [apache-cassandra, apache-kafka, etcd]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-DDS-0017]
related: [DBKB-SEC-0001]
aliases: [cluster security, inter-node encryption]
search_keywords: [TLS, mTLS, authentication, authorization, encryption at rest, audit]
risk: security-sensitive
version_sensitive: true
review_cycle: 6m
research_packages: [RP-DDS-0001]
source_ids: [SRC-000086, SRC-000087, SRC-000088]
acceptance_criteria: [Client/inter-node security, least privilege, secret rotation and audit controls are covered]
---
# Distributed Data Security

Secure both client-to-node és node-to-node trafficot TLS/mTLS-sel, és külön kezeld az authenticationt, authorizationt és encryption-at-restet. A certificate/key rotation legyen automatikus vagy runbookkal bizonyított, expiry alerttal.

Least privilege korlátozza a topic/keyspace/cluster admin műveleteket. Auditáld a data access-t, membership változást, configuration override-ot és bulk exportot; secretet ne írj logba vagy snapshotba.

## Források
- [Apache Cassandra Documentation](https://cassandra.apache.org/doc/latest/)
- [Apache Kafka Documentation](https://kafka.apache.org/documentation/)
- [etcd Documentation](https://etcd.io/docs/)
