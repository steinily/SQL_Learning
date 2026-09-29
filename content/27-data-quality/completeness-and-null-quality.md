---
schema_version: 1
id: DBKB-DQ-0005
title: Completeness and Null Quality
type: technology
primary_domain: data-quality
secondary_domains: [data-modeling]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [great-expectations, dbt, postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-DQ-0004]
related: []
aliases: [null completeness checks]
search_keywords: [completeness, null rate, missing value, required field]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-DQ-0001]
source_ids: [SRC-000077, SRC-000078]
acceptance_criteria: [Null/missing semantics, population and threshold are covered]
---
# Completeness and Null Quality

Completeness a required fields, records, partitions vagy expected source range presenceét méri; null, empty string, unknown sentinel és not-applicable értéket különítsd el. Threshold population, time window, late data allowance és remediation owner legyen explicit.

## Források
- [Great Expectations Documentation](https://docs.greatexpectations.io/docs/)
- [dbt — Data Tests](https://docs.getdbt.com/docs/build/tests)
