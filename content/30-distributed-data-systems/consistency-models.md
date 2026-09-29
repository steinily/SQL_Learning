---
schema_version: 1
id: DBKB-DDS-0005
title: Consistency Models
type: concept
primary_domain: distributed-data-systems
secondary_domains: [architecture, application-design]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [apache-cassandra, apache-kafka, etcd]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-DDS-0004]
related: [DBKB-DDS-0006, DBKB-DDS-0007]
aliases: [read consistency, write consistency]
search_keywords: [strong consistency, eventual consistency, read after write, stale read]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-DDS-0001]
source_ids: [SRC-000086, SRC-000087, SRC-000088]
acceptance_criteria: [Strong, eventual and application-visible consistency tradeoffs are explained]
---
# Consistency Models

Consistency model azt írja le, milyen értéket és milyen időzítéssel láthat a reader egy distributed write után. Strong consistency szigorúbb ordering/visibility elvárást ad; eventual consistency esetén a replicas convergence-e időt vesz igénybe, ezért stale read lehetséges.

A policy-t operation-szinten írd le: melyik adatnál elfogadható stale value, milyen read/write quorum vagy session guarantee kell, és hogyan kezeli az alkalmazás a conflictot. A termékek saját terminológiát és konfigurációt használnak, ezért a vendor semantics-et ne cseréld fel általános címkékkel.

## Források
- [Apache Cassandra Documentation](https://cassandra.apache.org/doc/latest/)
- [Apache Kafka Documentation](https://kafka.apache.org/documentation/)
- [etcd Documentation](https://etcd.io/docs/)
