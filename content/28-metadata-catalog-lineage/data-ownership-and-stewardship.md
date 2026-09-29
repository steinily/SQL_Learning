---
schema_version: 1
id: DBKB-META-0005
title: Data Ownership and Stewardship
type: playbook
primary_domain: metadata
secondary_domains: [governance]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [datahub, openlineage]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-META-0004]
related: []
aliases: [data steward operating model]
search_keywords: [data owner, steward, accountability, approval, escalation]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-META-0001]
source_ids: [SRC-000080, SRC-000082]
acceptance_criteria: [Owner/steward roles, accountability, review and escalation are defined]
---
# Data Ownership and Stewardship

Owner business accountabilityt, steward day-to-day definition/quality/metadatát, platform team pedig technical availabilityt kezelhet. Entityhez owner, steward, domain, review cadence, escalation, exception expiry és evidence tartozzon; catalog record owner nélkül governance gap.

## Források
- [DataHub Documentation](https://docs.datahub.com/)
- [OpenLineage Documentation](https://openlineage.io/docs/)
