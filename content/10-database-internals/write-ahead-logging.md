---
schema_version: 1
id: DBKB-INT-0005
title: Write Ahead Logging
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
prerequisites: [DBKB-INT-0002]
related: [DBKB-INT-0006, DBKB-INT-0016]
aliases: [WAL]
search_keywords: [WAL, write ahead log, durability, redo]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-INT-0001]
source_ids: [SRC-000014]
acceptance_criteria: [WAL durability és recovery szerepét leírja, execution claim nélkül]
---
# Write Ahead Logging

Write-ahead loggingben a log record durable storageba kerül, mielőtt a kapcsolódó data page tartósan kiírásra kerül. Ez teszi lehetővé crash recovery során a szükséges redo/undo mechanizmust; pontos flush és replication policy konfigurációfüggő.

## Források
- [PostgreSQL 18 — Write-Ahead Logging](https://www.postgresql.org/docs/18/wal.html)
