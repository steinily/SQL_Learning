---
schema_version: 1
id: DBKB-DQ-0013
title: Data Quality SLAs
type: concept
primary_domain: data-quality
secondary_domains: [governance, reliability]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [great-expectations, dbt]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-DQ-0012]
related: []
aliases: [data quality service level]
search_keywords: [quality SLA, threshold, freshness, defect budget, owner]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-DQ-0001]
source_ids: [SRC-000077, SRC-000078]
acceptance_criteria: [Quality objective, threshold, window, owner and breach response are defined]
---
# Data Quality SLAs

Quality SLA-ben metric, population, threshold, measurement window, freshness, severity, owner, exception és remediation time szerepeljen. Aggregate quality score ne rejtsen critical rule breach-et; SLA actual evidence és consumer impact alapján review-olandó.

## Források
- [Great Expectations Documentation](https://docs.greatexpectations.io/docs/)
- [dbt — Data Tests](https://docs.getdbt.com/docs/build/tests)
