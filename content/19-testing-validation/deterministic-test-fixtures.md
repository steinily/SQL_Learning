---
schema_version: 1
id: DBKB-TEST-0004
title: Deterministic Test Fixtures
type: technology
primary_domain: testing-validation
secondary_domains: [data-quality]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql, sqlite]
sql_dialects: [postgresql, tsql, mysql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-TEST-0002]
related: []
aliases: [test fixture design]
search_keywords: [deterministic fixture, seed data, isolation, cleanup]
risk: caution
version_sensitive: false
review_cycle: 6m
research_packages: [RP-TEST-0001]
source_ids: [SRC-000058]
acceptance_criteria: [Fixture identity, seed, isolation and cleanup are defined]
---
# Deterministic Test Fixtures

Deterministic fixture-ben stable IDs, explicit seed order, timezone, locale, constraints és expected row counts legyenek. Test isolated transaction vagy dedicated database/schema használjon, cleanup legyen idempotent, és fixture ne tartalmazzon production personal data-t.

## Források
- [PostgreSQL — Regression Tests](https://www.postgresql.org/docs/current/regress.html)
