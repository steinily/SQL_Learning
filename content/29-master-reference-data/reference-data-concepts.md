---
schema_version: 1
id: DBKB-MDM-0003
title: Reference Data Concepts
type: concept
primary_domain: reference-data
secondary_domains: [governance]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [openmetadata]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-MDM-0002]
related: []
aliases: [controlled reference values]
search_keywords: [reference data, code set, lookup, controlled vocabulary, validity]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-MDM-0001]
source_ids: [SRC-000083, SRC-000084]
acceptance_criteria: [Reference code set, labels, validity, mapping and ownership are covered]
---
# Reference Data Concepts

Reference data controlled code/value set, például country, currency, status vagy classification, amelyet rendszerek konzisztensen használnak. Concept scheme, notation/code, preferred label, valid-from/to, deprecated mapping, owner és consumer impact legyen versioned.

## Források
- [W3C SKOS](https://www.w3.org/TR/skos-reference/)
- [ISO 8000](https://www.iso.org/standard/50798.html)
