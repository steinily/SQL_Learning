---
schema_version: 1
id: DBKB-TEST-0018
title: CI Database Gates
type: technology
primary_domain: testing-validation
secondary_domains: [delivery]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-TEST-0016]
related: []
aliases: [database CI checks]
search_keywords: [CI gate, pipeline, migration gate, flaky test]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-TEST-0001]
source_ids: [SRC-000058, SRC-000059]
acceptance_criteria: [Pipeline ordering, isolation, artifacts and gate policy are defined]
---
# CI Database Gates

CI database gate legyen gyors metadata/schema check, unit/integration assertion, migration dry-run, regression subset és szükség szerint performance/security stage. Pipeline pinelje a engine/image versiont, artifactolja az evidence-et, kezelje a flaky testet explicit policy-val, és ne engedjen PASS-t unsupported environmentre.

## Források
- [PostgreSQL — Regression Tests](https://www.postgresql.org/docs/current/regress.html)
- [Microsoft SQL Server Documentation](https://learn.microsoft.com/en-us/sql/relational-databases/)
