---
schema_version: 1
id: DBKB-SS-0016
title: Temporary Tables
type: technology
primary_domain: sql-server
secondary_domains: [tsql]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [sqlserver]
sql_dialects: [tsql]
scope: vendor-specific
prerequisites: [DBKB-SS-0015]
related: [DBKB-SS-0017]
aliases: ["#temp table"]
search_keywords: ["SQL Server temporary table", tempdb, "#table"]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-SS-0001]
source_ids: [SRC-000030]
acceptance_criteria: [Local/global temp scope, tempdb impact és indexing trade-offot adja]
---
# Temporary Tables

Temporary table `tempdb`-ben materializált relation, amely session vagy procedure scope-ban élhet. Statistics/indexek előnyt adhatnak, de tempdb contention, cleanup és transaction impact mérendő.

## Források
- [Microsoft Learn — Temporary tables](https://learn.microsoft.com/sql/t-sql/data-types/table-transact-sql)
