---
schema_version: 1
id: DBKB-CAP-0070
title: Learning Path Relational Engineering
type: learning-path
primary_domain: capstone
secondary_domains: [relational-modeling, sql, operations]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql, sqlite]
sql_dialects: [postgresql, tsql, mysql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-CAP-0069]
related: [DBKB-CAP-0024, DBKB-CAP-0052]
aliases: [relational learning path]
search_keywords: [learning path, relational modeling, constraints, transactions, indexes]
risk: production-critical
version_sensitive: false
review_cycle: 12m
research_packages: [RP-CAPSTONE-0001]
source_ids: [SRC-000001]
acceptance_criteria: [Ordered relational engineering path with design, implementation and validation criteria is provided]
---
# Learning Path Relational Engineering

Sorrend: modeling glossary → ERD/keys/normalization → constraints → query exercise → transactions/isolation → indexes/performance → migration/backup → relational design case. Assessment artifact: DDL, query set, plan/lock evidence, recovery and ADR.

Exit criteria: learner links business invariant to schema/constraint/transaction, measures query behavior and documents reversible operational change.

## Forrás
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
