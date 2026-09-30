---
schema_version: 1
id: DBKB-CAP-0069
title: Learning Path SQL Foundations
type: learning-path
primary_domain: capstone
secondary_domains: [sql, learning]
levels: [beginner]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql, sqlite]
sql_dialects: [postgresql, tsql, mysql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-CAP-0068]
related: [DBKB-CAP-0023, DBKB-CAP-0046]
aliases: [SQL learning path]
search_keywords: [learning path, SQL foundations, SELECT, DML, DDL, "NULL"]
risk: safe
version_sensitive: false
review_cycle: 12m
research_packages: [RP-CAPSTONE-0001]
source_ids: [SRC-000001]
acceptance_criteria: [Ordered SQL foundations path with practice and assessment criteria is provided]
---
# Learning Path SQL Foundations

Sorrend: SQL glossary → SELECT/filter/join → aggregate/NULL → DDL/constraints → DML safety → transaction basics → SQL fundamentals exercise → assessment. Minden állomásnál query output, edge-case validation és dialect note szükséges.

Exit criteria: learner can explain result shape, choose constraints, write safe DML, identify NULL/duplicate behavior and document actual execution evidence.

## Forrás
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
