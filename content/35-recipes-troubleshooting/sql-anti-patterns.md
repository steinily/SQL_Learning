---
schema_version: 1
id: DBKB-REC-0041
title: SQL Anti-Patterns
type: error
primary_domain: recipes
secondary_domains: [sql, performance]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql, sqlite]
sql_dialects: [postgresql, tsql, mysql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-REC-0040]
related: [DBKB-PERF-0001]
aliases: [SQL mistakes]
search_keywords: [SQL anti-pattern, SELECT star, implicit conversion, N plus one, unbounded query]
risk: production-critical
version_sensitive: false
review_cycle: 12m
research_packages: [RP-RECIPES-0001]
source_ids: [SRC-000001]
acceptance_criteria: [SQL anti-patterns include detection signals and safe remediation]
---
# SQL Anti-Patterns

Gyakori anti-pattern: `SELECT *`, unbounded pagination/scan, implicit conversion, non-sargable predicate, N+1 query, dynamic SQL injection, missing parameterization, huge transaction és `UPDATE/DELETE` precheck nélkül.

Detectionhez query fingerprint, plan, row/scan ratio, lock/timeout, code review és static lint kell. Remediation legyen dialect-aware és regression testelt; ne adj vakon indexet vagy query hintet a root cause megértése nélkül.

## Forrás
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
