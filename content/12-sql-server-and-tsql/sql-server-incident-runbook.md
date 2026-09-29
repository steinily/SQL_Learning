---
schema_version: 1
id: DBKB-SS-0038
title: SQL Server Incident Runbook
type: playbook
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
prerequisites: [DBKB-SS-0032, DBKB-SS-0028]
related: [DBKB-SS-0040]
aliases: [SQL Server incident response]
search_keywords: [SQL Server incident, blocking incident, AG failover]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-SS-0001]
source_ids: [SRC-000030]
acceptance_criteria: [Safety, scope, waits, backup, mitigation, recovery és postmortem lépéseket ad]
---
# SQL Server Incident Runbook

Incident flow: impact/safety; active requests, waits és blocking; Query Store/Extended Events; recent deployment/configuration; reversible mitigation; backup/AG evidence; recovery/failover; communication; postmortem.

## Források
- [Microsoft Learn — Monitor SQL Server performance](https://learn.microsoft.com/sql/relational-databases/performance/monitor-and-tune-for-performance)
