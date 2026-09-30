---
schema_version: 1
id: DBKB-REC-0049
title: Distributed Systems Anti-Patterns
type: error
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
prerequisites: [DBKB-REC-0048]
related: [DBKB-DDS-0001]
aliases: [distributed data mistakes]
search_keywords: [split brain, retry storm, hot partition, quorum loss, global ordering]
risk: production-critical
version_sensitive: true
review_cycle: 12m
research_packages: [RP-RECIPES-0001]
source_ids: [SRC-000086, SRC-000087, SRC-000088]
acceptance_criteria: [Distributed failure anti-patterns include detection and bounded remediation]
---
# Distributed Systems Anti-Patterns

Anti-pattern a global ordering assumption, unbounded retry storm, hot partition, force-write quorum loss alatt, blind leader promotion, synchronous cross-region dependency és replica count failure domain nélkül.

Detectáld partition skew, lag, retry rate, quorum/leader health, network latency és recovery drift alapján. Containment throttle/fence/isolate; repair/replay csak known checkpoint, idempotency és reconciliation mellett.

## Források
- [Apache Cassandra Documentation](https://cassandra.apache.org/doc/latest/)
- [Apache Kafka Documentation](https://kafka.apache.org/documentation/)
- [etcd Documentation](https://etcd.io/docs/)
