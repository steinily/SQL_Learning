---
schema_version: 1
id: DBKB-TX-0014
title: Snapshot Visibility
type: concept
primary_domain: transactions-and-concurrency
secondary_domains: [concurrency]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-TX-0013]
related: [DBKB-TX-0007, DBKB-TX-0022]
aliases: [visibility snapshot, transaction snapshot]
search_keywords: [snapshot visibility, MVCC visibility, transaction ID]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-TX-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Visibility claimet statement és transaction snapshot különbségével ad]
---
# Snapshot Visibility

Visibility analysisnél rögzíteni kell az isolation levelt, a snapshot létrejöttének pontját, a concurrent commitokat és a statement sorrendet. Read Committed alatt statementenként változhat a látható állapot; magasabb szinteken hosszabb életű snapshot eltérő eredményt adhat.

Ezek a szabályok PostgreSQL dokumentációból származó vendor-specific állítások; más engine-re külön forrás szükséges.

## Források

- [PostgreSQL 18 — Transaction Isolation](https://www.postgresql.org/docs/18/transaction-iso.html)
