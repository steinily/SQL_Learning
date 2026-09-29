---
schema_version: 1
id: DBKB-PERF-0020
title: Partition Pruning
type: technology
primary_domain: query-performance
secondary_domains: [postgresql]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-PERF-0002]
related: [DBKB-PERF-0021]
aliases: [partition elimination]
search_keywords: [partition pruning, partition constraint, partitionwise]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-PERF-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Partition pruning plan evidence és predicate requirementet leírja]
---
# Partition Pruning

Partition pruning a partition constraint alapján kihagyja a nem releváns child relationöket. A predicate formája, parameter timing és partition key alignment meghatározza, hogy static vagy runtime pruning történik.

## Források
- [PostgreSQL 18 — Partition Pruning](https://www.postgresql.org/docs/18/ddl-partitioning.html#DDL-PARTITION-PRUNING)
