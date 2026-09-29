---
schema_version: 1
id: DBKB-STREAM-0004
title: Consumer Groups and Offsets
type: technology
primary_domain: streaming
secondary_domains: [messaging]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [apache-kafka]
sql_dialects: [postgresql, tsql, mysql]
scope: vendor-specific
prerequisites: [DBKB-STREAM-0003]
related: []
aliases: [Kafka consumer offset]
search_keywords: [consumer group, offset commit, lag, rebalance]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-STREAM-0001]
source_ids: [SRC-000069]
acceptance_criteria: [Group assignment, offsets, lag, rebalance and reset risks are explained]
---
# Consumer Groups and Offsets

Consumer group partition assignmenttal párhuzamosít, offset pedig processing progress-t jelöl. Commit timing, rebalance, pause, reset és crash recovery delivery semantics-t változtat; offset reset destructive lehet, ezért scope, backup/evidence és replay deduplication kell.

## Források
- [Apache Kafka Documentation](https://kafka.apache.org/documentation/)
