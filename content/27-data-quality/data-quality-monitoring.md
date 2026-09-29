---
schema_version: 1
id: DBKB-DQ-0010
title: Data Quality Monitoring
type: technology
primary_domain: data-quality
secondary_domains: [observability]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [great-expectations, dbt]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-DQ-0009]
related: []
aliases: [quality monitoring]
search_keywords: [quality score, expectation result, drift, alert, checkpoint]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-DQ-0001]
source_ids: [SRC-000077, SRC-000078]
acceptance_criteria: [Rule result, trend, drift, alert and ownership are covered]
---
# Data Quality Monitoring

Quality monitoring expectation resultot, failure rate, severity, trend/drift, freshness, volume, rule coverage és owner acknowledgementet követ. Alert threshold legyen actionable és windowed; quality score aggregáció ne fedje el critical rule failure-t vagy coverage gapet.

## Források
- [Great Expectations Documentation](https://docs.greatexpectations.io/docs/)
- [dbt — Data Tests](https://docs.getdbt.com/docs/build/tests)
