---
schema_version: 1
id: DBKB-TEST-0016
title: Test Evidence and Provenance
type: reference
primary_domain: testing-validation
secondary_domains: [governance]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-TEST-0015]
related: []
aliases: [test provenance]
search_keywords: [test evidence, execution record, provenance, reproducibility]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-TEST-0001]
source_ids: [SRC-000057, SRC-000058]
acceptance_criteria: [Execution identity, environment, inputs, outputs and hash/provenance are defined]
---
# Test Evidence and Provenance

Test evidence rögzítse a test ID-t, commit/buildet, engine versiont, environmentet, fixture hash-t, commandot, timestampot, actual resultot, expected resultot és status reason-t. Evidence provenance nélkül a PASS reprodukálhatatlan és audit szempontból gyenge.

## Források
- [NIST SP 800-115](https://csrc.nist.gov/publications/detail/sp/800-115/final)
- [PostgreSQL — Regression Tests](https://www.postgresql.org/docs/current/regress.html)
