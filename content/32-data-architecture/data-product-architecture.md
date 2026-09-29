---
schema_version: 1
id: DBKB-DARCH-0009
title: Data Product Architecture
type: technology
primary_domain: data-architecture
secondary_domains: [data-contracts, governance]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [dcat, data-mesh]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-DARCH-0008]
related: [DBKB-INTG-0001]
aliases: [data product]
search_keywords: [data product, contract, interface, SLO, ownership, discoverability]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-DARCH-0001]
source_ids: [SRC-000093, SRC-000094]
acceptance_criteria: [Product interface, owner, quality, security, documentation and support contract are defined]
---
# Data Product Architecture

Data product egy fogyasztható, discoverable data interface: schema/semantics, sample, owner, access path, quality/SLO, freshness, lineage, security classification, versioning és support channel tartozik hozzá.

Product boundaryn belül a producer kezeli a source pipeline-t és qualityt; consumer feedback, deprecation notice és compatibility policy védi az interface-t. Egy dashboard vagy raw table csak akkor product, ha ezeket a consumer-facing garanciákat teljesíti.

## Források
- [W3C DCAT](https://www.w3.org/TR/vocab-dcat-3/)
- [AWS Data Mesh Guidance](https://docs.aws.amazon.com/prescriptive-guidance/latest/modern-data-architectures/data-mesh.html)
