---
schema_version: 1
id: DBKB-NOSQL-0010
title: NoSQL Transactions
type: technology
primary_domain: nosql
secondary_domains: [data-integrity, application-design]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [mongodb, apache-cassandra]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-NOSQL-0009]
related: [DBKB-DDS-0010]
aliases: [document transaction]
search_keywords: [NoSQL transaction, atomic write, multi-document transaction, batch]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-NOSQL-0001]
source_ids: [SRC-000086, SRC-000089]
acceptance_criteria: [Atomicity scope, transaction cost, retry and alternative patterns are explained]
---
# NoSQL Transactions

Transaction előtt definiáld az atomicity scope-ot: egy key/document, partition, collection vagy több shard. A nagyobb scope általában több coordinationt és latency-t jelent; a vendor által támogatott boundary-t és retry semantics-et a release manual alapján ellenőrizd.

Ha a business invariant több aggregate-et érint, mérlegeld az event/outbox, Saga vagy compensating workflow-t. Commit timeout esetén az outcome lehet uncertain; idempotency key és read-back/reconciliation szükséges.

## Források
- [MongoDB Manual](https://www.mongodb.com/docs/manual/)
- [Apache Cassandra Documentation](https://cassandra.apache.org/doc/latest/)
