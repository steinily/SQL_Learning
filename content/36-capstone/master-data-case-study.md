---
schema_version: 1
id: DBKB-CAP-0017
title: Master Data Case Study
type: case-study
primary_domain: capstone
secondary_domains: [master-data, governance]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [openmetadata]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-CAP-0016]
related: [DBKB-MDM-0001]
aliases: [MDM case]
search_keywords: [golden record, matching, survivorship, steward, reference data]
risk: production-critical
version_sensitive: false
review_cycle: 12m
research_packages: [RP-CAPSTONE-0001]
source_ids: [SRC-000084, SRC-000085]
acceptance_criteria: [Scenario requires matching, golden record, governance, quality and integration decisions]
---
# Master Data Case Study

Customer és supplier source-ok conflicting identityt adnak. Tervezz matching/identifier rules-t, survivorship precedence-t, golden record provenance-t, steward exceptiont, reference lifecycle-t és downstream distributiont.

Elvárt evidence: match confidence, source values, merge decision, quality metric, audit trail, rollback és consumer reconciliation. Jogi identity vagy consent döntést domain/legal owner nélkül ne automatizálj.

## Források
- [ISO 8000 Data Quality](https://www.iso.org/standard/50798.html)
- [OpenMetadata Documentation](https://docs.open-metadata.org/)
