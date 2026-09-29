---
schema_version: 1
id: DBKB-DARCH-0014
title: Data Architecture Exercise
type: exercise
primary_domain: data-architecture
secondary_domains: [governance, platform-engineering]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [togaf, dcat, data-mesh]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-DARCH-0013]
related: [DBKB-DARCH-0005, DBKB-DARCH-0009]
aliases: [data architecture lab]
search_keywords: [data architecture exercise, ADR, data product, platform, governance]
risk: production-critical
version_sensitive: false
review_cycle: 12m
research_packages: [RP-DARCH-0001]
source_ids: [SRC-000092, SRC-000093, SRC-000094]
acceptance_criteria: [Learner produces target architecture, ADR, product contract, controls and transition plan]
---
# Data Architecture Exercise

Tervezd meg egy több domainből álló data platform target architecture-ját.

1. Rajzold fel a business/data/application/technology boundary-kat és ownershipet.
2. Definiálj egy data product contractot DCAT-szerű identityvel, quality/SLO-val, lineage-dzsel és access policy-vel.
3. Készíts ADR-t a centralized platform versus federated domain trade-offról.
4. Adj transition, security, observability, cost és rollback tervet.

Elvárt eredmény: context diagram, capability matrix, ADR, product card, governance gate és mérhető migration backlog.

## Források
- [The Open Group TOGAF Standard](https://pubs.opengroup.org/togaf-standard/)
- [W3C DCAT](https://www.w3.org/TR/vocab-dcat-3/)
- [AWS Data Mesh Guidance](https://docs.aws.amazon.com/prescriptive-guidance/latest/modern-data-architectures/data-mesh.html)
