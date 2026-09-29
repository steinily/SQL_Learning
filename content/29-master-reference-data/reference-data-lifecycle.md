---
schema_version: 1
id: DBKB-MDM-0009
title: Reference Data Lifecycle
type: playbook
primary_domain: master-data
secondary_domains: [governance, data-quality]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [openmetadata]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-MDM-0008]
related: [DBKB-MDM-0003]
aliases: [code set lifecycle, controlled vocabulary]
search_keywords: [reference data, code set, deprecation, effective date]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-MDM-0001]
source_ids: [SRC-000083, SRC-000084]
acceptance_criteria: [Proposal, approval, publication, deprecation and retirement states are described]
---
# Reference Data Lifecycle

Reference value lifecycle: proposed → reviewed → approved → published → deprecated → retired. A value should have a stable identifier, label, definition, owner, effective interval and replacement mapping where applicable.

Breaking changes are avoided by deprecating rather than silently reusing identifiers. Consumers validate unknown and expired codes, and migration plans document dual-read or dual-write periods. SKOS concept schemes provide a vocabulary model; local approval and retention rules remain domain responsibilities.

## Források
- [W3C SKOS Reference](https://www.w3.org/TR/skos-reference/)
- [ISO 8000 Data Quality](https://www.iso.org/standard/50798.html)
