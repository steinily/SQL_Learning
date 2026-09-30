---
schema_version: 1
id: DBKB-CAP-0022
title: Architecture Case Study
type: case-study
primary_domain: capstone
secondary_domains: [data-architecture, governance]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [togaf, dcat, data-mesh]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-CAP-0021]
related: [DBKB-DARCH-0001]
aliases: [architecture case]
search_keywords: [ADR, data platform, data product, governance, transition]
risk: production-critical
version_sensitive: false
review_cycle: 12m
research_packages: [RP-CAPSTONE-0001]
source_ids: [SRC-000092, SRC-000093, SRC-000094]
acceptance_criteria: [Scenario requires target architecture, domain boundary, governance, transition and risk decisions]
---
# Architecture Case Study

Egy szervezet central platform és federated data product operating model között választ. Készíts context/capability diagramot, domain boundary-t, ADR-t, governance gate-et, security/SLO/cost impactot és transition backlogot.

Elvárt evidence: options/trade-off, owner, interface/catalog, exception/expiry, observability és rollback. A case assumptions és actual organizational facts legyen külön jelölve.

## Források
- [The Open Group TOGAF Standard](https://pubs.opengroup.org/togaf-standard/)
- [W3C DCAT](https://www.w3.org/TR/vocab-dcat-3/)
- [AWS Data Mesh Guidance](https://docs.aws.amazon.com/prescriptive-guidance/latest/modern-data-architectures/data-mesh.html)
