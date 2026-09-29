---
schema_version: 1
id: DBKB-SS-0023
title: Execution Plans
type: concept
primary_domain: sql-server
secondary_domains: [performance]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [sqlserver]
sql_dialects: [tsql]
scope: vendor-specific
prerequisites: [DBKB-SS-0022]
related: [DBKB-PERF-0004]
aliases: [actual execution plan]
search_keywords: [SQL Server execution plan, estimated plan, actual plan]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-SS-0001]
source_ids: [SRC-000030]
acceptance_criteria: [Estimated/actual plan, operator cost és row estimate mismatch fogalmát adja]
---
# Execution Plans

Estimated plan statement futtatása nélkül, actual plan runtime metrics mellett készül. Operator, estimated/actual rows, memory grant, spills és warnings együtt olvasandó; graphical icon önmagában nem diagnosis.

## Források
- [Microsoft Learn — Display estimated execution plan](https://learn.microsoft.com/sql/relational-databases/performance/display-an-estimated-execution-plan)
