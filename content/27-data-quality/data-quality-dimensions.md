---
schema_version: 1
id: DBKB-DQ-0002
title: Data Quality Dimensions
type: concept
primary_domain: data-quality
secondary_domains: [governance]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [great-expectations, dbt]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-DQ-0001]
related: []
aliases: [quality dimensions]
search_keywords: [completeness, validity, accuracy, consistency, timeliness, uniqueness]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-DQ-0001]
source_ids: [SRC-000077, SRC-000079]
acceptance_criteria: [Dimensions and context-specific measurement are explained]
---
# Data Quality Dimensions

Common dimensions: completeness, validity, accuracy, consistency, uniqueness, timeliness/freshness, integrity és conformity. Dimension csak akkor hasznos, ha domain rule, population, measurement method, threshold, owner és remediation path tartozik hozzá.

## Források
- [Great Expectations Documentation](https://docs.greatexpectations.io/docs/)
- [NIST Big Data Interoperability Framework](https://www.nist.gov/publications/nist-big-data-interoperability-framework-volume-2-big-data-taxonomies)
