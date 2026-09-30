---
schema_version: 1
id: DBKB-CAP-0027
title: Index Exercise
type: exercise
primary_domain: capstone
secondary_domains: [performance, sql]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-CAP-0026]
related: [DBKB-IDX-0001]
aliases: [index tuning lab]
search_keywords: [index exercise, selectivity, composite index, explain, regression]
risk: production-critical
version_sensitive: true
review_cycle: 12m
research_packages: [RP-CAPSTONE-0001]
source_ids: [SRC-000001]
acceptance_criteria: [Learner compares index options with plan, write cost and rollback evidence]
---
# Index Exercise

Adj három query shape-hez index candidate-eket, majd hasonlítsd össze composite order, selectivity, write amplification, storage és plan output alapján.

Elvárt evidence: before/after explain, representative statistics, latency/resource, write impact, duplicate/unused analysis és rollback. Index improvement claim tényleges futtatással igazolandó.

## Forrás
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
