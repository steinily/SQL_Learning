---
schema_version: 1
id: DBKB-DQ-0008
title: Consistency and Reconciliation
type: playbook
primary_domain: data-quality
secondary_domains: [data-integration]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [great-expectations, dbt, postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-DQ-0007]
related: []
aliases: [data reconciliation]
search_keywords: [consistency, reconciliation, source target, control total, referential integrity]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-DQ-0001]
source_ids: [SRC-000077, SRC-000078]
acceptance_criteria: [Cross-system and intra-system consistency checks are defined]
---
# Consistency and Reconciliation

Consistency check source/target counts, control totals, key coverage, referential links, aggregate measures és event continuity szerint rétegezhető. Difference classification legyen source lag, duplicate, transform, missing, precision vagy scope mismatch; equal row count nem elégséges parity proof.

## Források
- [Great Expectations Documentation](https://docs.greatexpectations.io/docs/)
- [dbt — Data Tests](https://docs.getdbt.com/docs/build/tests)
