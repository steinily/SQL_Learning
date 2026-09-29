---
schema_version: 1
id: DBKB-DQ-0003
title: Data Quality Rules and Expectations
type: technology
primary_domain: data-quality
secondary_domains: [testing-validation]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [great-expectations, dbt]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-DQ-0002]
related: []
aliases: [data expectations]
search_keywords: [expectation, assertion, rule, threshold, severity]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-DQ-0001]
source_ids: [SRC-000077, SRC-000078]
acceptance_criteria: [Rule identity, scope, expected result, severity and evidence are defined]
---
# Data Quality Rules and Expectations

Rule/expectation tartalmazza a dataset/population scope-ot, expressiont, expected resultot, thresholdot, severityt, owner-t és run evidence-et. Generic null vagy row-count test csak részleges coverage; domain-specific invariant, relation és reconciliation rule is szükséges.

## Források
- [Great Expectations Documentation](https://docs.greatexpectations.io/docs/)
- [dbt — Data Tests](https://docs.getdbt.com/docs/build/tests)
