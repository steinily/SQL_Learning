---
schema_version: 1
id: DBKB-INT-0017
title: Crash Recovery
type: technology
primary_domain: database-internals
secondary_domains: [reliability]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-INT-0006, DBKB-INT-0016]
related: [DBKB-INT-0018]
aliases: [startup recovery, WAL replay]
search_keywords: [crash recovery, WAL replay, recovery target]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-INT-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Recovery sequence, evidence és RTO caveat-et ad]
---
# Crash Recovery

Crash recovery a durable checkpointből és WAL-ból építi vissza a konzisztens state-et. Recovery duration függ WAL mennyiségtől, I/O-tól és replay workloadtól; RTO-t csak tényleges restore/recovery drill bizonyít.

## Források
- [PostgreSQL 18 — WAL Internals](https://www.postgresql.org/docs/18/wal-internals.html)
