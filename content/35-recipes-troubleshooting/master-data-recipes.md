---
schema_version: 1
id: DBKB-REC-0021
title: Master Data Recipes
type: playbook
primary_domain: recipes
secondary_domains: [master-data, data-quality]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [openmetadata]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-REC-0020]
related: [DBKB-MDM-0001]
aliases: [MDM recipe]
search_keywords: [golden record, matching, survivorship, steward, reconciliation]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-RECIPES-0001]
source_ids: [SRC-000084, SRC-000085]
acceptance_criteria: [Matching, survivorship, governance, quality and reconciliation steps are actionable]
---
# Master Data Recipes

MDM recipeben identifier/matching inputot, confidence thresholdot, source precedence-t, survivorship rule-t és exception queue-t dokumentáld. Golden record publish előtt steward approval és losing source evidence maradjon auditban.

Quality breach esetén quarantine, duplicate merge dry-run, reconciliation, rollback és consumer notification kell. Catalog ownership/glossary frissítést ténylegesen verify-old, ne csak pipeline response alapján.

## Források
- [ISO 8000 Data Quality](https://www.iso.org/standard/50798.html)
- [OpenMetadata Documentation](https://docs.open-metadata.org/)
