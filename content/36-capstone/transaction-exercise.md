---
schema_version: 1
id: DBKB-CAP-0026
title: Transaction Exercise
type: exercise
primary_domain: capstone
secondary_domains: [transactions, reliability]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-CAP-0025]
related: [DBKB-TX-0001]
aliases: [transaction lab]
search_keywords: [transaction exercise, isolation, deadlock, retry, invariant]
risk: production-critical
version_sensitive: true
review_cycle: 12m
research_packages: [RP-CAPSTONE-0001]
source_ids: [SRC-000001]
acceptance_criteria: [Learner defines transaction boundary, isolation, failure tests and safe retry]
---
# Transaction Exercise

Implementáld egy inventory reservation transaction boundary-ját. Vizsgáld isolation level, lock order, timeout, deadlock/serialization failure, idempotency és compensation viselkedését.

Elvárt evidence: concurrent test, lock graph, invariant before/after, bounded retry és rollback/compensation. Az engine/version és execution output legyen rögzítve.

## Forrás
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
