---
schema_version: 1
id: DBKB-TEST-0002
title: Test Strategy for Databases
type: playbook
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
prerequisites: [DBKB-TEST-0001]
related: []
aliases: [database test plan]
search_keywords: [test strategy, risk-based testing, scope, entry exit criteria]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-TEST-0001]
source_ids: [SRC-000057]
acceptance_criteria: [Risk, scope, environments, entry/exit criteria and ownership are specified]
---
# Test Strategy for Databases

Test strategy-ben a risk-based scope, test levels, supported versions, representative data, isolation, entry/exit criteria, ownership és defect severity szerepeljen. A production-like testhez authorization, data handling és rollback constraints explicit módon szükséges.

## Források
- [NIST SP 800-115](https://csrc.nist.gov/publications/detail/sp/800-115/final)
