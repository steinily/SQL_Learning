---
schema_version: 1
id: DBKB-TEST-0003
title: Test Pyramid for Data Systems
type: concept
primary_domain: testing-validation
secondary_domains: [quality]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-TEST-0002]
related: []
aliases: [database test levels]
search_keywords: [unit test, integration test, end-to-end test, test pyramid]
risk: caution
version_sensitive: false
review_cycle: 6m
research_packages: [RP-TEST-0001]
source_ids: [SRC-000057]
acceptance_criteria: [Test level trade-offs and feedback speed are explained]
---
# Test Pyramid for Data Systems

A data system test pyramid alján gyors unit és schema checks, középen integration/contract tests, tetején lassabb end-to-end, performance és recovery tests állnak. A magasabb szintű testet ne használd az alacsonyabb determinisztikus assertionök helyett; mindegyik más kockázatot fed le.

## Források
- [NIST SP 800-115](https://csrc.nist.gov/publications/detail/sp/800-115/final)
