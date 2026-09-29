---
schema_version: 1
id: DBKB-IDX-0006
title: Covering Indexes
type: concept
primary_domain: indexing
secondary_domains: [performance]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-IDX-0003]
related: [DBKB-IDX-0016]
aliases: [index-only coverage]
search_keywords: [covering index, INCLUDE, index-only scan]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-IDX-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Covering/index-only scan feltételeit visibility caveat-tel adja meg]
---
# Covering Indexes

Covering index a lekérdezéshez szükséges oszlopokat az indexben elérhetővé teszi, így lehetővé tehet index-only scan-t. PostgreSQL-ben a visibility map és heap állapot is befolyásolja, hogy ténylegesen elkerülhető-e a heap access.

## Források
- [PostgreSQL 18 — Index-Only Scans](https://www.postgresql.org/docs/18/indexes-index-only-scans.html)
