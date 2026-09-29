---
schema_version: 1
id: DBKB-SS-0026
title: Locking and Blocking
type: troubleshooting
primary_domain: sql-server
secondary_domains: [concurrency]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [sqlserver]
sql_dialects: [tsql]
scope: vendor-specific
prerequisites: [DBKB-SS-0025]
related: [DBKB-SS-0027]
aliases: [blocking session, deadlock]
search_keywords: [SQL Server blocking, lock escalation, deadlock]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-SS-0001]
source_ids: [SRC-000030]
acceptance_criteria: [Lock modes, blocking, escalation és deadlock diagnosis evidence-et adja]
---
# Locking and Blocking

SQL Server lock compatibility, lock escalation és transaction duration együtt hat a blockingra. Diagnózisnál blocker/blocked session, resource, wait duration és transaction state kell; remediation csak captured evidence alapján.

## Források
- [Microsoft Learn — Transaction locking and row versioning guide](https://learn.microsoft.com/sql/relational-databases/sql-server-transaction-locking-and-row-versioning-guide)
