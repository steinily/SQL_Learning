---
schema_version: 1
id: DBKB-INT-0021
title: System Catalogs
type: technology
primary_domain: database-internals
secondary_domains: [postgresql]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-INT-0002]
related: [DBKB-PERF-0025]
aliases: [pg_catalog, system tables]
search_keywords: [system catalog, pg_class, pg_stat, catalog query]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-INT-0001]
source_ids: [SRC-000014]
acceptance_criteria: [System catalog és monitoring view különbségét vendor scope-ban adja]
---
# System Catalogs

System catalogs a database metadata authoritative belső reprezentációi; monitoring views részben ezekre vagy statisztikai subsystemsre épülnek. Catalog schema version-sensitive, ezért application integrationhez stabil documented view-t válassz.

## Források
- [PostgreSQL 18 — System Catalogs](https://www.postgresql.org/docs/18/catalogs.html)
