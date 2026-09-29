---
schema_version: 1
id: DBKB-DARCH-0003
title: Architecture Domains and Boundaries
type: concept
primary_domain: data-architecture
secondary_domains: [architecture, governance]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [togaf]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-DARCH-0002]
related: [DBKB-DARCH-0007]
aliases: [business data domain]
search_keywords: [business domain, data domain, bounded context, ownership boundary]
risk: production-critical
version_sensitive: false
review_cycle: 12m
research_packages: [RP-DARCH-0001]
source_ids: [SRC-000092, SRC-000094]
acceptance_criteria: [Business, data, application and technology boundaries with ownership are explained]
---
# Architecture Domains and Boundaries

Az architecture domain-ek elválasztása segít, hogy a business capability, data semantics, application behavior és technology implementation ne keveredjen. A boundary legyen ownership, interface, data classification, SLO és change authority szerint explicit.

Cross-domain data flow-nál jelöld a producer/consumer, contract, lineage, access policy és failure ownership kapcsolatot. A boundary nem feltétlenül szervezeti chart: egy team több domainben lehet owner, ha a decision rights dokumentáltak.

## Források
- [The Open Group TOGAF Standard](https://pubs.opengroup.org/togaf-standard/)
- [AWS Data Mesh Guidance](https://docs.aws.amazon.com/prescriptive-guidance/latest/modern-data-architectures/data-mesh.html)
