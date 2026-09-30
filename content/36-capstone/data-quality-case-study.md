---
schema_version: 1
id: DBKB-CAP-0012
title: Data Quality Case Study
type: case-study
primary_domain: capstone
secondary_domains: [data-quality, governance]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, openmetadata]
sql_dialects: [postgresql]
scope: cross-vendor
prerequisites: [DBKB-CAP-0011]
related: [DBKB-DQ-0001]
aliases: [quality case]
search_keywords: [data quality, duplicate, completeness, freshness, remediation]
risk: production-critical
version_sensitive: false
review_cycle: 12m
research_packages: [RP-CAPSTONE-0001]
source_ids: [SRC-000001, SRC-000085]
acceptance_criteria: [Scenario requires rule design, thresholds, quarantine, remediation and evidence]
---
# Data Quality Case Study

Customer datasetben duplicate, missing, stale és invalid reference values jelennek meg. Definiálj quality dimensions/rule-okat, threshold/severityt, quarantine és steward workflow-t, majd reconciliation és trend validationt.

Elvárt evidence: rule version, sample/full result, owner SLA, source/root cause, correction/replay és downstream impact. Threshold módosítás legyen reviewed change, ne silent workaround.

## Források
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [OpenMetadata Documentation](https://docs.open-metadata.org/)
