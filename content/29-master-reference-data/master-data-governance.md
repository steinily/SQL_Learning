---
schema_version: 1
id: DBKB-MDM-0008
title: Master Data Governance
type: playbook
primary_domain: master-data
secondary_domains: [governance, security]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [openmetadata]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-MDM-0007]
related: [DBKB-MDM-0009, DBKB-META-0008]
aliases: [data stewardship, master data operating model]
search_keywords: [steward, owner, policy, approval, master data governance]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-MDM-0001]
source_ids: [SRC-000084, SRC-000085]
acceptance_criteria: [Roles, decision rights, quality controls and escalation path are defined]
---
# Master Data Governance

A governance operating model rögzítse a data owner, data steward, custodian és consumer felelősségét. A policy-k legyenek mérhetők: identity resolution, completeness, validity, timeliness és duplicate rate küszöbökkel.

Change proposal esetén legyen impact analysis, jóváhagyó, effective date, rollback terv és audit trail. A catalog glossary, ownership és domain metadata támogatja a felfedezhetőséget, de nem helyettesíti a domain döntési fórumot.

## Források
- [ISO 8000 Data Quality](https://www.iso.org/standard/50798.html)
- [OpenMetadata Documentation](https://docs.open-metadata.org/)
