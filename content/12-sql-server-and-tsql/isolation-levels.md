---
schema_version: 1
id: DBKB-SS-0025
title: Isolation Levels
type: technology
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
prerequisites: [DBKB-SS-0024]
related: [DBKB-TX-0006, DBKB-SS-0026]
aliases: [READ COMMITTED, SNAPSHOT, RCSI]
search_keywords: [SQL Server isolation level, snapshot isolation, read committed snapshot]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-SS-0001]
source_ids: [SRC-000030]
acceptance_criteria: [Isolation choices, row versioning/locking és anomaly scopeját adja]
---
# Isolation Levels

SQL Server isolation setting locking vagy row-versioning behaviorrel befolyásolja dirty/nonrepeatable/phantom read és blocking kockázatát. `READ_COMMITTED_SNAPSHOT` database option és `SNAPSHOT` transaction semantics külön konfigurációt igényel.

## Források
- [Microsoft Learn — SET TRANSACTION ISOLATION LEVEL](https://learn.microsoft.com/sql/t-sql/statements/set-transaction-isolation-level-transact-sql)
