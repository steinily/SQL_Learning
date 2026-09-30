---
schema_version: 1
id: DBKB-CAP-0029
title: SQL Server Exercise
type: exercise
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
prerequisites: [DBKB-CAP-0028]
related: [DBKB-RDBE-0001]
aliases: [SQL Server lab]
search_keywords: [SQL Server exercise, T-SQL, waits, index, backup]
risk: production-critical
version_sensitive: true
review_cycle: 12m
research_packages: [RP-CAPSTONE-0001]
source_ids: [SRC-000001]
acceptance_criteria: [Learner documents T-SQL plan, waits, log, security and recovery checks]
---
# SQL Server Exercise

T-SQL labban mérj query plan/waits, transaction log headroomot, blockingot, index hatást és backup/restore validációt. Documentáld compatibility level, edition/version, config és permission boundary-t.

Elvárt evidence: commands/output, before/after metrics, invariant/permission test és rollback. Microsoft tooling vagy feature outputot csak actual execution után jelöld.

## Forrás
- [Microsoft SQL Server Documentation](https://learn.microsoft.com/sql/sql-server/)
