---
schema_version: 1
id: DBKB-SS-0033
title: SQL Server Performance
type: playbook
primary_domain: sql-server
secondary_domains: [performance]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [sqlserver]
sql_dialects: [tsql]
scope: vendor-specific
prerequisites: [DBKB-SS-0022, DBKB-SS-0032]
related: [DBKB-SS-0034]
aliases: [SQL Server tuning]
search_keywords: [SQL Server performance, query tuning, wait stats, memory grant]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-SS-0001]
source_ids: [SRC-000030]
acceptance_criteria: [Baseline, plan, waits, indexes, statistics és resource workflowet adja]
---
# SQL Server Performance

SQL Server tuning workflow: baseline és workload; Query Store/actual plan; waits, CPU, I/O és memory grant; statistics/index; controlled change; representative re-measurement; rollback. Cost estimate nem wall-clock bizonyíték.

## Források
- [Microsoft Learn — Monitor and tune for performance](https://learn.microsoft.com/sql/relational-databases/performance/monitor-and-tune-for-performance)
