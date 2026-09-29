---
schema_version: 1
id: DBKB-DARCH-0007
title: Data Mesh Architecture
type: technology
primary_domain: data-architecture
secondary_domains: [governance, platform-engineering]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [data-mesh]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-DARCH-0006]
related: [DBKB-DARCH-0009]
aliases: [domain-oriented data architecture]
search_keywords: [data mesh, domain ownership, federated governance, self service]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-DARCH-0001]
source_ids: [SRC-000094]
acceptance_criteria: [Domain ownership, data as product, federated governance and platform are distinguished]
---
# Data Mesh Architecture

Data mesh négy gyakorlati concernje: domain ownership, data as a product, federated computational governance és self-service data platform. Ez operating model és architecture pattern együtt, nem automatikus decentralizáció.

Domain productnak legyen owner, contract, quality/SLO, discoverability, access policy, version és support path. Federated rule-ek a cross-domain interoperabilityt/securityt védik, de ne blokkolják minden local döntést; exception és appeal process szükséges.

## Forrás
- [AWS Data Mesh Guidance](https://docs.aws.amazon.com/prescriptive-guidance/latest/modern-data-architectures/data-mesh.html)
