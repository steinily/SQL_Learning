---
schema_version: 1
id: DBKB-REC-0012
title: SQL Server Recipes
type: technology
primary_domain: recipes
secondary_domains: [sql-server, operations]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [sql-server]
sql_dialects: [tsql]
scope: vendor-specific
prerequisites: [DBKB-REC-0011]
related: [DBKB-RDBE-0001]
aliases: [T-SQL cookbook]
search_keywords: [SQL Server recipe, T-SQL, execution plan, lock, index]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-RECIPES-0001]
source_ids: [SRC-000001]
acceptance_criteria: [T-SQL-specific safety, plan validation, locking and recovery cautions are documented]
---
# SQL Server Recipes

T-SQL recipeben capture-old a database compatibility levelt, isolationt, active locks/waits, transaction log headroomot és execution plan baseline-t. `SET XACT_ABORT`, explicit transaction és bounded batch csak az adott workload és error semantics ellenőrzése után használható.

Index/DDL, statistics update és bulk DML előtt evaluate-old blocking, log growth, HA/replication impact és rollbacket. SQL Server feature/version/edition behavior változhat; official Microsoft documentation és actual execution output szükséges.

## Forrás
- [Microsoft SQL Server Documentation](https://learn.microsoft.com/sql/sql-server/)
