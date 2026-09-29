---
schema_version: 1
id: DBKB-DARCH-0002
title: Data Architecture Principles
type: concept
primary_domain: data-architecture
secondary_domains: [governance, data-quality]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [togaf]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-DARCH-0001]
related: [DBKB-DARCH-0005]
aliases: [architecture principles]
search_keywords: [data principle, ownership, interoperability, reuse, least privilege]
risk: production-critical
version_sensitive: false
review_cycle: 12m
research_packages: [RP-DARCH-0001]
source_ids: [SRC-000092, SRC-000093, SRC-000094]
acceptance_criteria: [Actionable principles include ownership, interoperability, quality, security and evolution]
---
# Data Architecture Principles

Használj explicit principle-ket: data owner és steward accountability; contract-first interoperability; fit-for-purpose quality; least privilege; source-of-truth clarity; reuse before duplication; lifecycle és retention; observable, reversible change.

Egy principle akkor hasznos, ha decision rule, exception process, measurable indicator és review owner tartozik hozzá. A „single source of truth” ne legyen abszolút slogan: domainenként és attribute-onként jelöld a source precedence-t.

## Források
- [The Open Group TOGAF Standard](https://pubs.opengroup.org/togaf-standard/)
- [W3C DCAT](https://www.w3.org/TR/vocab-dcat-3/)
- [AWS Data Mesh Guidance](https://docs.aws.amazon.com/prescriptive-guidance/latest/modern-data-architectures/data-mesh.html)
