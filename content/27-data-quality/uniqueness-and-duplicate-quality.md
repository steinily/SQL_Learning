---
schema_version: 1
id: DBKB-DQ-0006
title: Uniqueness and Duplicate Quality
type: technology
primary_domain: data-quality
secondary_domains: [data-integration]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [great-expectations, dbt, postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-DQ-0005]
related: []
aliases: [duplicate detection]
search_keywords: [uniqueness, duplicate, natural key, deduplication, collision]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-DQ-0001]
source_ids: [SRC-000077, SRC-000078]
acceptance_criteria: [Key scope, duplicate definition, collision and remediation are described]
---
# Uniqueness and Duplicate Quality

Uniqueness key scope-t, grain-t és time window-t követel: business key, composite key, event ID vagy current-row constraint eltérő duplicate semantics-t ad. Duplicate detection után classify-old legitimate repeatet, source replayt és true collisiont, és idempotent remediationt használj.

## Források
- [Great Expectations Documentation](https://docs.greatexpectations.io/docs/)
- [dbt — Data Tests](https://docs.getdbt.com/docs/build/tests)
