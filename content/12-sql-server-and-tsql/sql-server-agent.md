---
schema_version: 1
id: DBKB-SS-0030
title: SQL Server Agent
type: technology
primary_domain: sql-server
secondary_domains: [operations]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [sqlserver]
sql_dialects: [tsql]
scope: vendor-specific
prerequisites: [DBKB-SS-0003]
related: [DBKB-SS-0032]
aliases: [Agent job]
search_keywords: [SQL Server Agent, job, schedule, alert, operator]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-SS-0001]
source_ids: [SRC-000030]
acceptance_criteria: [Job step, schedule, proxy, credential, alert és failure handling scopeját adja]
---
# SQL Server Agent

SQL Server Agent jobokkal scheduled T-SQL, SSIS vagy PowerShell lépéseket futtat. Job owner, proxy/credential, retry, alert, output retention és idempotency legyen explicit; sysadmin ownership anti-pattern.

## Források
- [Microsoft Learn — SQL Server Agent](https://learn.microsoft.com/sql/ssms/agent/sql-server-agent)
