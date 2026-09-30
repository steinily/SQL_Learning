---
schema_version: 1
id: DBKB-CAP-0013
title: Metadata Lineage Case Study
type: case-study
primary_domain: capstone
secondary_domains: [metadata, governance]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [openmetadata, openlineage]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-CAP-0012]
related: [DBKB-META-0001]
aliases: [lineage case]
search_keywords: [metadata, lineage, ownership, catalog, impact analysis]
risk: production-critical
version_sensitive: true
review_cycle: 12m
research_packages: [RP-CAPSTONE-0001]
source_ids: [SRC-000080, SRC-000085]
acceptance_criteria: [Scenario requires catalog, lineage freshness, ownership and change impact evidence]
---
# Metadata Lineage Case Study

Egy critical dataset upstream schema change után hibás downstream dashboardot eredményez; catalog lineage részben stale. Elemezd asset identityt, event/run/dataset lineage-t, owner/stewardot és consumer impactot.

Elvárt evidence: last-seen/freshness, lineage graph, changed revision, affected consumer, correction és catalog update verification. Catalog API success nem bizonyít lineage completeness-t.

## Források
- [OpenLineage Documentation](https://openlineage.io/docs/)
- [OpenMetadata Documentation](https://docs.open-metadata.org/)
