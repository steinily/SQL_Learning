---
schema_version: 1
id: DBKB-DARCH-0006
title: Data Platform Architecture
type: technology
primary_domain: data-architecture
secondary_domains: [platform-engineering, operations]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [dcat, togaf]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-DARCH-0005]
related: [DBKB-DARCH-0007]
aliases: [data platform]
search_keywords: [data platform, ingestion, storage, compute, catalog, self service]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-DARCH-0001]
source_ids: [SRC-000092, SRC-000093, SRC-000094]
acceptance_criteria: [Platform capability layers, tenancy, interfaces, SLO and ownership are described]
---
# Data Platform Architecture

Data platform capability layers: ingestion/integration, durable storage, processing/serving, catalog/lineage, quality/security és developer self-service. A platform product interface-t és paved path-ot ad; nem veszi át a domain owner üzleti felelősségét.

Architecture decisionnél mérd a isolationt, elasticityt, cost, reliabilityt, support modellt és exit path-et. Minden shared service-hez API/contract, SLO, tenancy boundary, quota, incident owner és lifecycle kell.

## Források
- [The Open Group TOGAF Standard](https://pubs.opengroup.org/togaf-standard/)
- [W3C DCAT](https://www.w3.org/TR/vocab-dcat-3/)
- [AWS Data Mesh Guidance](https://docs.aws.amazon.com/prescriptive-guidance/latest/modern-data-architectures/data-mesh.html)
