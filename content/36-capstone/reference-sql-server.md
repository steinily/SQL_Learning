---
schema_version: 1
id: DBKB-CAP-0049
title: Reference SQL Server
type: reference
primary_domain: capstone
secondary_domains: [sql-server, operations]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [sql-server]
sql_dialects: [tsql]
scope: vendor-specific
prerequisites: [DBKB-CAP-0048]
related: [DBKB-RDBE-0001]
aliases: [SQL Server quick reference]
search_keywords: [SQL Server reference, T-SQL, wait, plan, log, HA]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-CAPSTONE-0001]
source_ids: [SRC-000001]
acceptance_criteria: [SQL Server navigation, T-SQL, plan, security, HA and recovery controls are summarized]
---
# Reference SQL Server

Navigation: T-SQL/DDL/DML; execution plans/waits; indexes/statistics; transactions/locking; roles; transaction log; backup/restore; HA/replication; Agent/monitoring.

Always record engine version, edition, compatibility level and feature prerequisites. Validate plan, blocking, log, permission and recovery impact before production execution.

## Forrás
- [Microsoft SQL Server Documentation](https://learn.microsoft.com/sql/sql-server/)
