---
schema_version: 1
id: DBKB-INT-0006
title: Checkpoints and Recovery
type: technology
primary_domain: database-internals
secondary_domains: [durability]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-INT-0005]
related: [DBKB-INT-0017]
aliases: [checkpoint recovery]
search_keywords: [checkpoint, crash recovery, recovery point]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-INT-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Checkpoint, WAL replay és recovery duration kapcsolatát magyarázza]
---
# Checkpoints and Recovery

Checkpoint a dirty buffers és recovery metadata kontrollált tartósítási pontja. Crash után a recovery a checkpoint és az azt követő WAL alapján állítja helyre a konzisztens állapotot; duration és I/O a workloadtól függ.

## Források
- [PostgreSQL 18 — Checkpoints](https://www.postgresql.org/docs/18/wal-configuration.html)
