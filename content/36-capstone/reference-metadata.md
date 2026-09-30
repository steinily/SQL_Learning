---
schema_version: 1
id: DBKB-CAP-0062
title: Reference Metadata
type: reference
primary_domain: capstone
secondary_domains: [metadata, governance]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [openmetadata, openlineage]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-CAP-0061]
related: [DBKB-META-0001]
aliases: [metadata checklist]
search_keywords: [metadata reference, catalog, lineage, ownership, glossary, freshness]
risk: production-critical
version_sensitive: true
review_cycle: 12m
research_packages: [RP-CAPSTONE-0001]
source_ids: [SRC-000080, SRC-000085]
acceptance_criteria: [Catalog identity, ownership, lineage, classification and lifecycle checklist is provided]
---
# Reference Metadata

Checklist: stable asset identity; technical/business metadata; owner/steward/domain; tags/glossary; classification; quality; lineage/provenance; freshness; lifecycle/retention; access; audit; retirement.

Catalog API response nem bizonyít completeness-t; ellenőrizd target queryvel, last-seen/event freshness-szel és consumer impacttal.

## Források
- [OpenLineage Documentation](https://openlineage.io/docs/)
- [OpenMetadata Documentation](https://docs.open-metadata.org/)
