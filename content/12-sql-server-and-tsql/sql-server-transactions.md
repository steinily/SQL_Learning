---
schema_version: 1
id: DBKB-SS-0024
title: SQL Server Transactions
type: concept
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
prerequisites: [DBKB-SS-0011]
related: [DBKB-SS-0025, DBKB-SS-0026]
aliases: [BEGIN TRAN, COMMIT, ROLLBACK]
search_keywords: [SQL Server transaction, XACT_STATE, TRY CATCH]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-SS-0001]
source_ids: [SRC-000030]
acceptance_criteria: [Explicit/implicit transaction, XACT_STATE és rollback boundaryt adja]
---
# SQL Server Transactions

T-SQL explicit transaction `BEGIN TRANSACTION`–`COMMIT`/`ROLLBACK` boundaryt ad; `XACT_STATE()` hibás vagy committable állapotot különböztet meg. Nested transaction syntax nem azonos valódi nested atomic unit-tal.

## Források
- [Microsoft Learn — Transactions (Transact-SQL)](https://learn.microsoft.com/sql/t-sql/language-elements/transactions-transact-sql)
