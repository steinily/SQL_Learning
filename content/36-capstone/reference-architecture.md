---
schema_version: 1
id: DBKB-CAP-0068
title: Reference Architecture
type: reference
primary_domain: capstone
secondary_domains: [data-architecture, governance]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [togaf, dcat, data-mesh]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-CAP-0067]
related: [DBKB-DARCH-0001]
aliases: [architecture checklist]
search_keywords: [architecture reference, ADR, domain, platform, data product, governance]
risk: production-critical
version_sensitive: false
review_cycle: 12m
research_packages: [RP-CAPSTONE-0001]
source_ids: [SRC-000092, SRC-000093, SRC-000094]
acceptance_criteria: [Architecture context, boundary, decision, governance, security and transition checklist is provided]
---
# Reference Architecture

Checklist: business/data/application/technology boundary; owner; capability; interface/product; ADR/options; security; quality/SLO; lineage; cost; observability; lifecycle; exception/expiry; transition; rollback.

Diagram, catalog vagy platform label önmagában nem architecture evidence; döntést, owner-t, trade-offot és mérhető validationt is őrizz.

## Források
- [The Open Group TOGAF Standard](https://pubs.opengroup.org/togaf-standard/)
- [W3C DCAT](https://www.w3.org/TR/vocab-dcat-3/)
- [AWS Data Mesh Guidance](https://docs.aws.amazon.com/prescriptive-guidance/latest/modern-data-architectures/data-mesh.html)
