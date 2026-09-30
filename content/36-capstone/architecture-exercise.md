---
schema_version: 1
id: DBKB-CAP-0045
title: Architecture Exercise
type: exercise
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
prerequisites: [DBKB-CAP-0044]
related: [DBKB-DARCH-0001]
aliases: [architecture lab]
search_keywords: [architecture exercise, ADR, data product, platform, transition]
risk: production-critical
version_sensitive: false
review_cycle: 12m
research_packages: [RP-CAPSTONE-0001]
source_ids: [SRC-000092, SRC-000093, SRC-000094]
acceptance_criteria: [Learner produces context, target architecture, ADR, governance, security and transition artifacts]
---
# Architecture Exercise

Tervezd meg central platform és federated data product model kombinációját. Készíts context/capability diagramot, domain boundary-t, data product cardot, ADR-t és governance review gate-et.

Adj SLO, security, cost, observability, exception expiry, migration és rollback tervet. Assumptions, official source claims és actual organizational evidence legyen elkülönítve.

## Források
- [The Open Group TOGAF Standard](https://pubs.opengroup.org/togaf-standard/)
- [W3C DCAT](https://www.w3.org/TR/vocab-dcat-3/)
- [AWS Data Mesh Guidance](https://docs.aws.amazon.com/prescriptive-guidance/latest/modern-data-architectures/data-mesh.html)
