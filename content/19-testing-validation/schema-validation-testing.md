---
schema_version: 1
id: DBKB-TEST-0009
title: Schema Validation Testing
type: technology
primary_domain: testing-validation
secondary_domains: [data-modeling]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-TEST-0008]
related: []
aliases: [database schema tests]
search_keywords: [schema validation, constraints, indexes, metadata assertion]
risk: caution
version_sensitive: true
review_cycle: 6m
research_packages: [RP-TEST-0001]
source_ids: [SRC-000058, SRC-000059]
acceptance_criteria: [Tables, constraints, indexes, grants and metadata are testable]
---
# Schema Validation Testing

Schema validation ellenőrizze tables, columns, types, nullability, keys, foreign keys, indexes, views, routines és grants állapotát. Golden schema diff előtt kezeld az engine defaults és generated metadata eltéréseit, és különítsd el az intentional migration change-et a drift-től.

## Források
- [PostgreSQL — Regression Tests](https://www.postgresql.org/docs/current/regress.html)
- [Microsoft SQL Server Documentation](https://learn.microsoft.com/en-us/sql/relational-databases/)
