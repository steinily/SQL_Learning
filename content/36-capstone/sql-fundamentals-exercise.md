---
schema_version: 1
id: DBKB-CAP-0023
title: SQL Fundamentals Exercise
type: exercise
primary_domain: capstone
secondary_domains: [sql, learning]
levels: [beginner]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql, sqlite]
sql_dialects: [postgresql, tsql, mysql, sqlite]
scope: portable-sql
prerequisites: [DBKB-CAP-0022]
related: [DBKB-SQL-0001]
aliases: [SQL basics lab]
search_keywords: [SQL exercise, SELECT, WHERE, JOIN, GROUP BY, "NULL"]
risk: safe
version_sensitive: false
review_cycle: 12m
research_packages: [RP-CAPSTONE-0001]
source_ids: [SRC-000001]
acceptance_criteria: [Learner writes validated SELECT, filter, join, aggregate and null-handling queries]
---
# SQL Fundamentals Exercise

Egy customer/order/product dataseten írj query-ket: projection/filter, inner/outer join, aggregate/grouping, `NULL` kezelés és deterministic ordering.

Minden queryhez add meg expected columns, sample result shape, edge cases és validation checket. A dialect-specific syntaxot jelöld; execution evidence nélkül a megoldás csak proposed.

## Forrás
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
