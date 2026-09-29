---
schema_version: 1
id: DBKB-DQ-0018
title: Data Quality Exercise
type: exercise
primary_domain: data-quality
secondary_domains: [validation]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [great-expectations, dbt, postgresql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-DQ-0017]
related: []
aliases: [data quality exercise]
search_keywords: [quality exercise, expectation suite, quarantine, reconciliation]
risk: caution
version_sensitive: false
review_cycle: 6m
research_packages: [RP-DQ-0001]
source_ids: [SRC-000077, SRC-000078, SRC-000079]
acceptance_criteria: [Exercise defines evidence without claiming unexecuted results]
---
# Data Quality Exercise

Tervezd meg egy dataset validation flow-t null/duplicate, schema drift, freshness breach és source-target reconciliation hibával. Készíts expectation/rule inventoryt, severity/SLA döntést, quarantine/backfill path-ot, evidence indexet és owner communicationt; execution-verified csak valódi futtatás után használható.

## Források
- [Great Expectations Documentation](https://docs.greatexpectations.io/docs/)
- [dbt — Data Tests](https://docs.getdbt.com/docs/build/tests)
