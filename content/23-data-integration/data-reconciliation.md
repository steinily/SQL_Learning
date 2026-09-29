---
schema_version: 1
id: DBKB-INTG-0014
title: Data Reconciliation
type: playbook
primary_domain: data-integration
secondary_domains: [data-quality]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [apache-kafka, debezium, postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-INTG-0013]
related: []
aliases: [integration reconciliation]
search_keywords: [reconciliation, source target parity, count check, hash total]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-INT-0001]
source_ids: [SRC-000069, SRC-000070]
acceptance_criteria: [Count, aggregate, key and semantic reconciliation are described]
---
# Data Reconciliation

Reconciliation rétegzett legyen: count/volume, aggregate totals, key coverage, event/offset continuity, row-level hash/sample és domain semantic check. Difference esetén scope-old source lag, duplicate, delete, late data, transform bug vagy partial write okát; egy matching count nem bizonyít parity-t.

## Források
- [Apache Kafka Documentation](https://kafka.apache.org/documentation/)
- [Debezium Documentation](https://debezium.io/documentation/)
