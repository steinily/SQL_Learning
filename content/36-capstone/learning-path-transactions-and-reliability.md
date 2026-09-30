---
schema_version: 1
id: DBKB-CAP-0074
title: Learning Path Transactions and Reliability
type: learning-path
primary_domain: capstone
secondary_domains: [transactions, reliability]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, apache-kafka]
sql_dialects: [postgresql]
scope: cross-vendor
prerequisites: [DBKB-CAP-0073]
related: [DBKB-CAP-0026, DBKB-CAP-0038]
aliases: [reliability path]
search_keywords: [learning path, transaction, deadlock, backup, RPO, RTO]
risk: production-critical
version_sensitive: false
review_cycle: 12m
research_packages: [RP-CAPSTONE-0001]
source_ids: [SRC-000001, SRC-000087]
acceptance_criteria: [Ordered transaction/reliability path with failure, recovery and evidence milestones]
---
# Learning Path Transactions and Reliability

Sorrend: ACID/invariants → isolation/locks/deadlocks → idempotent retry/outbox → backup/restore → replication/failover → recovery exercise/case → incident evidence.

Exit criteria: bounded retry, known recovery boundary, RPO/RTO, business correctness validation and post-incident action plan.

## Források
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [Apache Kafka Documentation](https://kafka.apache.org/documentation/)
