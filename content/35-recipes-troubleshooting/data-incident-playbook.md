---
schema_version: 1
id: DBKB-REC-0055
title: Data Incident Playbook
type: playbook
primary_domain: recipes
secondary_domains: [data-quality, operations]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, apache-kafka, openmetadata]
sql_dialects: [postgresql]
scope: cross-vendor
prerequisites: [DBKB-REC-0054]
related: [DBKB-DQ-0001]
aliases: [data correctness incident]
search_keywords: [data incident, wrong data, duplicate, quarantine, reconciliation]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-RECIPES-0001]
source_ids: [SRC-000001, SRC-000080]
acceptance_criteria: [Wrong/missing/duplicate data containment, correction, reconciliation and communication are defined]
---
# Data Incident Playbook

Freeze or quarantine affected publish pathot, identify dataset/window/consumer blast radiust, preserve source and output evidence-et. Classify wrong, missing, duplicate, stale or unauthorized data incidentként, majd assign owner és severity.

Correction csak known source/checkpointból, idempotent replayjel vagy approved compensationnel. Validate row/count/checksum/quality/business invariant és downstream consumer state-et; communicate affected windows and residual uncertainty.

## Források
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [OpenLineage Documentation](https://openlineage.io/docs/)
