---
schema_version: 1
id: DBKB-CAP-0006
title: SQL Server Operations Case Study
type: case-study
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
prerequisites: [DBKB-CAP-0005]
related: [DBKB-RDBE-0001]
aliases: [SQL Server case]
search_keywords: [SQL Server operations, wait stats, log growth, HA, backup]
risk: production-critical
version_sensitive: true
review_cycle: 12m
research_packages: [RP-CAPSTONE-0001]
source_ids: [SRC-000001]
acceptance_criteria: [Scenario requires SQL Server wait, transaction log, HA/backup and recovery decisions]
---
# SQL Server Operations Case Study

Egy SQL Server workloadnél log growth, blocking és HA replica lag jelentkezik. Elemezd wait/lock evidence-et, transaction log/backup chain-t, compatibility levelt, failover readiness-t és RPO/RTO-t.

Elvárt evidence: query/plan, wait graph, log space, replica state, backup freshness, containment, rollback és recovery validation. Microsoft release/edition behavior és execution result csak linked evidence-szel állítható.

## Forrás
- [Microsoft SQL Server Documentation](https://learn.microsoft.com/sql/sql-server/)
