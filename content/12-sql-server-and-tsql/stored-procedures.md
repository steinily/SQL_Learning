---
schema_version: 1
id: DBKB-SS-0011
title: Stored Procedures
type: technology
primary_domain: sql-server
secondary_domains: [programming]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [sqlserver]
sql_dialects: [tsql]
scope: vendor-specific
prerequisites: [DBKB-SS-0010]
related: [DBKB-SS-0012, DBKB-SS-0024]
aliases: [CREATE PROCEDURE]
search_keywords: [T-SQL stored procedure, parameters, output parameter]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-SS-0001]
source_ids: [SRC-000030]
acceptance_criteria: [Procedure parameters, result sets, transaction és security scopeját adja]
---
# Stored Procedures

Stored procedure paraméterezett T-SQL routine, amely result setet, output paramétert és transaction interactiont adhat. Caller contract, SET options, permissions, error handling és plan behavior legyen dokumentált.

## Források
- [Microsoft Learn — CREATE PROCEDURE](https://learn.microsoft.com/sql/t-sql/statements/create-procedure-transact-sql)
