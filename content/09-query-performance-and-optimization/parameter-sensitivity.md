---
schema_version: 1
id: DBKB-PERF-0014
title: Parameter Sensitivity
type: troubleshooting
primary_domain: query-performance
secondary_domains: [application-design]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-PERF-0013]
related: [DBKB-PERF-0027, DBKB-PERF-0028]
aliases: [parameter-sensitive plan]
search_keywords: [parameter sensitivity, generic plan, custom plan]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-PERF-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Parameter value distribution és plan variation caveat-et ad]
---
# Parameter Sensitivity

Ugyanaz a prepared query különböző parameter value-k mellett eltérő optimális access pathot igényelhet. Diagnosztikáld representative value set-tel, plan cache és execution evidence alapján; egyetlen parameterből ne általánosíts.

## Források
- [PostgreSQL 18 — PREPARE](https://www.postgresql.org/docs/18/sql-prepare.html)
