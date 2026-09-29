---
schema_version: 1
id: DBKB-DQ-0001
title: Data Quality Overview
type: overview
primary_domain: data-quality
secondary_domains: [governance, testing-validation]
levels: [beginner]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [great-expectations, dbt, postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-TEST-0001]
related: []
aliases: [data quality overview]
search_keywords: [data quality, expectation, validation, rule, owner]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-DQ-0001]
source_ids: [SRC-000077, SRC-000078, SRC-000079]
acceptance_criteria: [Quality scope, dimensions, ownership and execution evidence are defined]
---
# Data Quality Overview

Data quality data consumerének declared expectationjeihez viszonyított mérhető fitness: rules, dimensions, time window, severity, owner és remediation evidence kell. Green pipeline vagy schema-valid output nem bizonyítja a business accuracy-t és completeness-t.

## Források
- [Great Expectations Documentation](https://docs.greatexpectations.io/docs/)
- [dbt — Data Tests](https://docs.getdbt.com/docs/build/tests)
