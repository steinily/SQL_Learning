---
schema_version: 1
id: DBKB-MDM-0014
title: Master and Reference Data Exercise
type: exercise
primary_domain: master-data
secondary_domains: [data-quality, governance]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [openmetadata]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-MDM-0013]
related: [DBKB-MDM-0007, DBKB-MDM-0011]
aliases: [MDM lab]
search_keywords: [MDM exercise, golden record, survivorship, quality rule]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-MDM-0001]
source_ids: [SRC-000084, SRC-000085]
acceptance_criteria: [Learner designs matching, survivorship, quality and audit controls with evidence]
---
# Master and Reference Data Exercise

Tervezd meg egy customer master flow-t három source-szal és egy országkód reference set-tel.

1. Definiáld az identifier, matching és survivorship szabályokat; nevezd meg a kivételeket.
2. Írd le a reference value lifecycle-t, ownerét és deprecation mappingjét.
3. Adj meg legalább négy quality rule-t thresholdtal és remediation ownerrel.
4. Készíts reconciliation és audit evidence checklistet egy sikertelen publish után.

Elvárt eredmény: döntési táblázat, lifecycle diagram, quality rule lista és incident runbook. A megoldást domain owner review-val és reprodukálható tesztmintákkal validáld.

## Források
- [ISO 8000 Data Quality](https://www.iso.org/standard/50798.html)
- [OpenMetadata Documentation](https://docs.open-metadata.org/)
