---
schema_version: 1
id: DBKB-DQ-0014
title: Data Quality Testing
type: playbook
primary_domain: data-quality
secondary_domains: [testing-validation]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [great-expectations, dbt]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-DQ-0013]
related: []
aliases: [quality test strategy]
search_keywords: [quality test, expectation suite, fixture, sampling, regression]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-DQ-0001]
source_ids: [SRC-000077, SRC-000078]
acceptance_criteria: [Unit, integration, regression, sampling and execution evidence are covered]
---
# Data Quality Testing

Quality testben deterministic fixture, rule/expectation, schema, relation, reconciliation, freshness, distribution/drift és regression checks legyenek. Sampling scope, false negative risk, test data version, actual result és failure artifact explicit; test PASS nem bizonyít untested populationt.

## Források
- [Great Expectations Documentation](https://docs.greatexpectations.io/docs/)
- [dbt — Data Tests](https://docs.getdbt.com/docs/build/tests)
