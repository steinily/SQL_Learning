---
schema_version: 1
id: DBKB-IDX-0012
title: Index Maintenance
type: troubleshooting
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
prerequisites: [DBKB-IDX-0001]
related: [DBKB-IDX-0013, DBKB-IDX-0014]
aliases: [index upkeep, REINDEX]
search_keywords: [index maintenance, reindex, vacuum, analyze]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-IDX-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Maintenance műveleteket és online/offline trade-offot dokumentál]
---
# Index Maintenance

Index maintenance része a statistics frissítése, a bloat megfigyelése és szükség esetén a rebuild vagy `REINDEX`. A művelet lock, I/O és replication hatását production környezetben előre mérni kell.

## Források
- [PostgreSQL 18 — REINDEX](https://www.postgresql.org/docs/18/sql-reindex.html)
