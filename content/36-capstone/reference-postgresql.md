---
schema_version: 1
id: DBKB-CAP-0048
title: Reference PostgreSQL
type: reference
primary_domain: capstone
secondary_domains: [postgresql, operations]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-CAP-0047]
related: [DBKB-PG-0001]
aliases: [PostgreSQL quick reference]
search_keywords: [PostgreSQL reference, EXPLAIN, VACUUM, WAL, role, backup]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-CAPSTONE-0001]
source_ids: [SRC-000001]
acceptance_criteria: [PostgreSQL navigation, core operations and safety controls are summarized]
---
# Reference PostgreSQL

Navigation: SQL/DDL/DML; `EXPLAIN`; indexes/statistics; transactions/locks; `VACUUM`; roles/privileges; WAL/replication; backup/restore; configuration and monitoring.

Check exact server version and extension/config prerequisites. Destructive or production-critical operation needs precheck, backup/recovery boundary, post-validation and official release documentation.

## Forrás
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
