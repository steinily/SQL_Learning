---
schema_version: 1
id: DBKB-TX-0013
title: MVCC and Snapshots
type: technology
primary_domain: transactions-and-concurrency
secondary_domains: [postgresql]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-TX-0006]
related: [DBKB-TX-0014, DBKB-TX-0022]
aliases: [multi-version concurrency control, MVCC]
search_keywords: [MVCC, snapshot, row version]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-TX-0001]
source_ids: [SRC-000014]
acceptance_criteria: [MVCC snapshot és visibility alapfogalmakat PostgreSQL scope-ban definiál]
---
# MVCC and Snapshots

Az MVCC több row version használatával választja el az olvasókat és írókat. PostgreSQL-ben az isolation level meghatározza, hogy egy statement vagy egy transaction milyen snapshotot lát.

Az MVCC nem jelenti azt, hogy nincs lock vagy hogy minden workload lock-free. A vacuum, bloat és long-running transaction hatása külön operational vizsgálat.

## Források

- [PostgreSQL 18 — Transaction Isolation](https://www.postgresql.org/docs/18/transaction-iso.html)
