---
schema_version: 1
id: DBKB-TEST-0006
title: Integration Testing Databases
type: technology
primary_domain: testing-validation
secondary_domains: [integration]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-TEST-0005]
related: []
aliases: [database integration tests]
search_keywords: [integration test, transaction boundary, driver, migration]
risk: caution
version_sensitive: true
review_cycle: 6m
research_packages: [RP-TEST-0001]
source_ids: [SRC-000058, SRC-000059]
acceptance_criteria: [Application-driver-schema integration and cleanup are described]
---
# Integration Testing Databases

Integration test a real driver, transaction boundary, schema, migration, authentication és serialization behaviorét együtt ellenőrzi. Environment version, connection pool, timezone és cleanup explicit legyen; embedded SQLite csak akkor használható substitutionként, ha a semantics ténylegesen kompatibilis.

## Források
- [PostgreSQL — Regression Tests](https://www.postgresql.org/docs/current/regress.html)
- [Microsoft SQL Server Documentation](https://learn.microsoft.com/en-us/sql/relational-databases/)
