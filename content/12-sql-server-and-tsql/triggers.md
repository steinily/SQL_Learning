---
schema_version: 1
id: DBKB-SS-0013
title: Triggers
type: technology
primary_domain: sql-server
secondary_domains: [data-integrity]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [sqlserver]
sql_dialects: [tsql]
scope: vendor-specific
prerequisites: [DBKB-SS-0011]
related: [DBKB-SS-0024]
aliases: [DML trigger, DDL trigger]
search_keywords: [SQL Server trigger, inserted, deleted, trigger recursion]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-SS-0001]
source_ids: [SRC-000030]
acceptance_criteria: [DML/DDL trigger timing, inserted/deleted és hidden side effectet adja]
---
# Triggers

SQL Server DML trigger statement-level eseményhez kapcsolódik, és `inserted`/`deleted` logical tables alapján dolgozik. Multi-row statement, recursion, transaction scope és hidden writes miatt trigger behavior legyen explicit tesztelve.

## Források
- [Microsoft Learn — DML triggers](https://learn.microsoft.com/sql/relational-databases/triggers/dml-triggers)
