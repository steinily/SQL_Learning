---
schema_version: 1
id: DBKB-TEST-0020
title: Testing and Validation Exercise
type: exercise
primary_domain: testing-validation
secondary_domains: [validation]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-TEST-0015, DBKB-TEST-0018]
related: []
aliases: [database validation exercise]
search_keywords: [testing exercise, migration gate, failure injection, evidence]
risk: caution
version_sensitive: false
review_cycle: 6m
research_packages: [RP-TEST-0001]
source_ids: [SRC-000057, SRC-000058]
acceptance_criteria: [Exercise defines evidence without claiming unexecuted results]
---
# Testing and Validation Exercise

Építs CI validation plan-t egy schema migration, data-quality assertion, concurrency scenario és recovery drill számára. Rögzíts fixture hash-t, engine/versiont, expected/actual resultot, failure artifactot, gate decisiont és retestet; execution-verified csak tényleges futtatás után jelölhető.

## Források
- [NIST SP 800-115](https://csrc.nist.gov/publications/detail/sp/800-115/final)
- [PostgreSQL — Regression Tests](https://www.postgresql.org/docs/current/regress.html)
