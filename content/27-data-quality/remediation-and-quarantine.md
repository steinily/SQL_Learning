---
schema_version: 1
id: DBKB-DQ-0012
title: Remediation and Quarantine
type: playbook
primary_domain: data-quality
secondary_domains: [reliability]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [great-expectations, dbt, apache-kafka]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-DQ-0011]
related: []
aliases: [bad data quarantine]
search_keywords: [remediation, quarantine, reject, correction, replay, backfill]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-DQ-0001]
source_ids: [SRC-000077, SRC-000078]
acceptance_criteria: [Quarantine, correction, replay, approval and verification are specified]
---
# Remediation and Quarantine

Quarantine preserve-olja a bad row/event, failure reason, source identity, rule version és arrival contextet; remediation lehet correction, source fix, backfill, replay vagy reject. Release csak revalidation, reconciliation, owner approval és downstream impact review után történjen.

## Források
- [Great Expectations Documentation](https://docs.greatexpectations.io/docs/)
- [dbt — Data Tests](https://docs.getdbt.com/docs/build/tests)
