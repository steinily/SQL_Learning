---
schema_version: 1
id: DBKB-CAP-0035
title: Quality Exercise
type: exercise
primary_domain: capstone
secondary_domains: [data-quality, governance]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, openmetadata]
sql_dialects: [postgresql]
scope: cross-vendor
prerequisites: [DBKB-CAP-0034]
related: [DBKB-DQ-0001]
aliases: [quality lab]
search_keywords: [quality exercise, completeness, duplicate, freshness, remediation]
risk: production-critical
version_sensitive: false
review_cycle: 12m
research_packages: [RP-CAPSTONE-0001]
source_ids: [SRC-000001, SRC-000085]
acceptance_criteria: [Learner defines rules, thresholds, quarantine, remediation and trend evidence]
---
# Quality Exercise

Definiálj completeness, validity, uniqueness, referential, timeliness és reconciliation rule-t egy customer datasetre, threshold/severity/owner/SLA értékekkel.

Injectálj duplicate, null, invalid code és late batch hibát; ellenőrizd quarantine, steward workflow, correction/replay és post-fix trendet. Evidence: rule version, result counts, samples és downstream impact.

## Források
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [OpenMetadata Documentation](https://docs.open-metadata.org/)
