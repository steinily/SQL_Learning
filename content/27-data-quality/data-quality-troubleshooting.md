---
schema_version: 1
id: DBKB-DQ-0016
title: Data Quality Troubleshooting
type: troubleshooting
primary_domain: data-quality
secondary_domains: [operations]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [great-expectations, dbt]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-DQ-0015]
related: []
aliases: [quality failure diagnosis]
search_keywords: [quality failure, false positive, schema drift, source lag, rule bug]
risk: caution
version_sensitive: false
review_cycle: 6m
research_packages: [RP-DQ-0001]
source_ids: [SRC-000077, SRC-000078]
acceptance_criteria: [Failure classification, evidence preservation and rerun discipline are defined]
---
# Data Quality Troubleshooting

Quality failuret source/data issue, schema drift, rule defect, fixture/environment, late data, duplicate, threshold change vagy orchestration failure kategóriába sorold. Preserve-eld failed batch, rule version, sample/evidence és population scope-ot; blind threshold increase nem remediation.

## Források
- [Great Expectations Documentation](https://docs.greatexpectations.io/docs/)
- [dbt — Data Tests](https://docs.getdbt.com/docs/build/tests)
