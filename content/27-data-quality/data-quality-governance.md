---
schema_version: 1
id: DBKB-DQ-0015
title: Data Quality Governance
type: playbook
primary_domain: data-quality
secondary_domains: [governance]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [great-expectations, dbt]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-DQ-0014]
related: []
aliases: [quality governance]
search_keywords: [quality owner, rule lifecycle, exception, lineage, stewardship]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-DQ-0001]
source_ids: [SRC-000077, SRC-000078, SRC-000079]
acceptance_criteria: [Ownership, rule lifecycle, exceptions, evidence and review are defined]
---
# Data Quality Governance

Governance-ban data owner/steward, rule owner, consumer, severity taxonomy, change/review lifecycle, exception expiry, evidence retention és escalation legyen. Quality rule catalog és lineage nélkül duplicated checks, conflicting thresholds és unowned failures alakulhatnak ki.

## Források
- [Great Expectations Documentation](https://docs.greatexpectations.io/docs/)
- [NIST Big Data Interoperability Framework](https://www.nist.gov/publications/nist-big-data-interoperability-framework-volume-2-big-data-taxonomies)
