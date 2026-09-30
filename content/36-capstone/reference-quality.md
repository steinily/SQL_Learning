---
schema_version: 1
id: DBKB-CAP-0061
title: Reference Quality
type: reference
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
prerequisites: [DBKB-CAP-0060]
related: [DBKB-DQ-0001]
aliases: [quality checklist]
search_keywords: [quality reference, completeness, validity, uniqueness, timeliness, reconciliation]
risk: production-critical
version_sensitive: false
review_cycle: 12m
research_packages: [RP-CAPSTONE-0001]
source_ids: [SRC-000001, SRC-000085]
acceptance_criteria: [Quality dimensions, rules, thresholds, ownership and remediation checklist is provided]
---
# Reference Quality

Checklist: dimension/rule/scope/window; threshold/severity/owner/SLA; source evidence; completeness/validity/uniqueness/referential/timeliness; quarantine; correction/replay; trend; downstream reconciliation; audit.

Quality score csak explicit dataset/window és rule version mellett értelmezhető; business correctnesset invariant és consumer validation egészítse ki.

## Források
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [OpenMetadata Documentation](https://docs.open-metadata.org/)
