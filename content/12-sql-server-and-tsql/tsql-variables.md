---
schema_version: 1
id: DBKB-SS-0009
title: T-SQL Variables
type: concept
primary_domain: sql-server
secondary_domains: [tsql]
levels: [intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [sqlserver]
sql_dialects: [tsql]
scope: vendor-specific
prerequisites: [DBKB-SS-0008]
related: [DBKB-SS-0010]
aliases: [DECLARE variable]
search_keywords: [T-SQL variable, DECLARE, SET, SELECT assignment]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-SS-0001]
source_ids: [SRC-000030]
acceptance_criteria: [DECLARE, assignment, scope és NULL behavior témáit adja]
---
# T-SQL Variables

T-SQL local variable batch/procedure scope-ban él; `DECLARE`, `SET` és `SELECT` assignment külön semantics-et adhat több sor, NULL és no-row esetén. Assignment contractot explicit teszteld.

## Források
- [Microsoft Learn — DECLARE @local_variable](https://learn.microsoft.com/sql/t-sql/language-elements/declare-local-variable-transact-sql)
