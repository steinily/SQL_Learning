---
schema_version: 1
id: DBKB-DQ-0017
title: Data Quality Runbook
type: playbook
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
prerequisites: [DBKB-DQ-0016]
related: []
aliases: [quality operations runbook]
search_keywords: [quality runbook, quarantine, backfill, rerun, release]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-DQ-0001]
source_ids: [SRC-000077, SRC-000078]
acceptance_criteria: [Prechecks, failure, quarantine, remediation, validation and communication are specified]
---
# Data Quality Runbook

Runbook tartalmazza dataset/rule identityt, expected windowt, prechecket, failure triage-t, quarantine/stop decisiont, source fixet, backfill/replayt, revalidationt, reconciliationt, release approvalt és communicationt. A commandokat target adapteren és data scope-on kell ellenőrizni.

## Források
- [Great Expectations Documentation](https://docs.greatexpectations.io/docs/)
- [dbt — Data Tests](https://docs.getdbt.com/docs/build/tests)
