---
schema_version: 1
id: DBKB-CAP-0025
title: SQL Query Exercise
type: exercise
primary_domain: capstone
secondary_domains: [sql, performance]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-CAP-0024]
related: [DBKB-PERF-0001]
aliases: [query lab]
search_keywords: [SQL query exercise, window function, CTE, explain, pagination]
risk: production-critical
version_sensitive: true
review_cycle: 12m
research_packages: [RP-CAPSTONE-0001]
source_ids: [SRC-000001]
acceptance_criteria: [Learner solves analytical query, pagination and performance validation tasks]
---
# SQL Query Exercise

Írj window functiont top-N és running total feladatra, CTE-t staged transformationre, keyset paginationt és egy duplicate-detection query-t. Definiáld expected semantics-t null/empty/tie esetén.

Mérd az execution plan/resource profile-t representative data-val; a tuning changehez baseline, hypothesis, correctness és rollback tartozzon. Ne állíts benchmarkot tényleges output nélkül.

## Forrás
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
