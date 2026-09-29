---
schema_version: 1
id: DBKB-SS-0035
title: T-SQL Exercise 1
type: exercise
primary_domain: sql-server
secondary_domains: [practice]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [sqlserver]
sql_dialects: [tsql]
scope: vendor-specific
prerequisites: [DBKB-SS-0023, DBKB-SS-0033]
related: [DBKB-SS-0036]
aliases: [SQL Server tuning lab]
search_keywords: [T-SQL exercise, execution plan lab, Query Store lab]
risk: safe
version_sensitive: true
review_cycle: 12m
research_packages: [RP-SS-0001]
source_ids: [SRC-000030]
acceptance_criteria: [Estimated/actual plan, Query Store baseline és tuning reportot gyakoroltat]
---
# T-SQL Exercise 1

Készíts staging exercise reportot: capture Query Store baseline-t, gyűjts estimated és actual execution plant, azonosíts egy row-estimate vagy index problémát, majd dokumentáld a controlled change és after measurement eredményét.

## Források
- [Microsoft Learn — Query Store](https://learn.microsoft.com/sql/relational-databases/performance/monitoring-performance-by-using-the-query-store)
