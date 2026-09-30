---
schema_version: 1
id: DBKB-CAP-0063
title: Reference Master Data
type: reference
primary_domain: capstone
secondary_domains: [master-data, governance]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [openmetadata]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-CAP-0062]
related: [DBKB-MDM-0001]
aliases: [MDM checklist]
search_keywords: [master data reference, golden record, matching, survivorship, steward]
risk: production-critical
version_sensitive: false
review_cycle: 12m
research_packages: [RP-CAPSTONE-0001]
source_ids: [SRC-000084, SRC-000085]
acceptance_criteria: [Master/reference lifecycle, matching, survivorship, quality and governance checklist is provided]
---
# Reference Master Data

Checklist: entity/identifier; source precedence; matching/confidence; golden record provenance; survivorship; steward/owner; reference lifecycle; quality thresholds; security; integration; reconciliation; audit/rollback.

Jogi identity, consent vagy regulatory decision ne legyen implicit automated merge; domain/legal owner és evidence szükséges.

## Források
- [ISO 8000 Data Quality](https://www.iso.org/standard/50798.html)
- [OpenMetadata Documentation](https://docs.open-metadata.org/)
