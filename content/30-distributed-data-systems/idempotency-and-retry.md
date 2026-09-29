---
schema_version: 1
id: DBKB-DDS-0011
title: Idempotency and Retry
type: playbook
primary_domain: distributed-data-systems
secondary_domains: [reliability, application-design]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [apache-cassandra, apache-kafka, etcd]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-DDS-0010]
related: [DBKB-OPS-0008]
aliases: [deduplication key, safe retry]
search_keywords: [idempotency, retry, backoff, duplicate request, deduplication]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-DDS-0001]
source_ids: [SRC-000086, SRC-000087, SRC-000088]
acceptance_criteria: [Retry safety, idempotency key, backoff and duplicate suppression are actionable]
---
# Idempotency and Retry

Retry csak akkor biztonságos, ha az operation idempotent vagy deduplication key védi. A client tartsa meg a request identity-t, a server pedig definiálja, meddig őrzi a completed resultot és mi történik timeout utáni uncertain outcome esetén.

Exponential backoff, jitter, bounded attempts és circuit breaking védje a cluster-t. Ne retry-old automatikusan a validation vagy authorization hibákat; különítsd el a transport timeoutot, leader change-et, overloadot és definitive rejectiont.

## Források
- [Apache Cassandra Documentation](https://cassandra.apache.org/doc/latest/)
- [Apache Kafka Documentation](https://kafka.apache.org/documentation/)
- [etcd Documentation](https://etcd.io/docs/)
