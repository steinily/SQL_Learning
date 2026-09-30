---
schema_version: 1
id: DBKB-CAP-0040
title: Master Data Exercise
type: exercise
primary_domain: capstone
secondary_domains: [master-data, data-quality]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [openmetadata]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-CAP-0039]
related: [DBKB-MDM-0001]
aliases: [MDM lab]
search_keywords: [MDM exercise, matching, survivorship, golden record, stewardship]
risk: production-critical
version_sensitive: false
review_cycle: 12m
research_packages: [RP-CAPSTONE-0001]
source_ids: [SRC-000084, SRC-000085]
acceptance_criteria: [Learner designs matching, survivorship, governance, quality and reconciliation controls]
---
# Master Data Exercise

Három customer source-ból tervezz identifier/matching, confidence, survivorship, golden record provenance, steward exception és downstream publish szabályt.

Adj quality rule-okat threshold/owner/SLA-val, reference lifecycle-t és duplicate merge rollbacket. Evidence: source values, decision table, audit trail, quality trend és reconciliation output.

## Források
- [ISO 8000 Data Quality](https://www.iso.org/standard/50798.html)
- [OpenMetadata Documentation](https://docs.open-metadata.org/)
