---
schema_version: 1
id: DBKB-DQ-0011
title: Data Quality Incident Response
type: playbook
primary_domain: data-quality
secondary_domains: [incident-management]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [great-expectations, dbt]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-DQ-0010]
related: []
aliases: [data incident response]
search_keywords: [quality incident, impact assessment, containment, communication]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-DQ-0001]
source_ids: [SRC-000077, SRC-000078]
acceptance_criteria: [Triage, impact, containment, correction and communication are defined]
---
# Data Quality Incident Response

Quality incidentnél scope-old affected dataset/consumer/windowt, preserve-old failed evidence-et, állítsd meg vagy quarantine-old a downstream publish-t, kommunikáld uncertainty-t, majd correction/backfill/reconciliation és post-incident review következzen. Rule failure severity nem automatikusan business impact.

## Források
- [Great Expectations Documentation](https://docs.greatexpectations.io/docs/)
- [dbt — Data Tests](https://docs.getdbt.com/docs/build/tests)
