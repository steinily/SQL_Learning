---
schema_version: 1
id: DBKB-IDX-0014
title: Concurrent Index Builds
type: technology
primary_domain: indexing
secondary_domains: [operations]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-IDX-0012]
related: [DBKB-IDX-0013]
aliases: [CREATE INDEX CONCURRENTLY]
search_keywords: [concurrent index build, online index creation]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-IDX-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Concurrent build lock/trade-off caveat-et ad]
---
# Concurrent Index Builds

`CREATE INDEX CONCURRENTLY` csökkentheti a write blockingot, de hosszabb ideig, több erőforrással és eltérő transaction szabályokkal futhat. A failed vagy invalid index állapotot külön monitorozni kell.

## Források
- [PostgreSQL 18 — Building Indexes Concurrently](https://www.postgresql.org/docs/18/sql-createindex.html#SQL-CREATEINDEX-CONCURRENTLY)
