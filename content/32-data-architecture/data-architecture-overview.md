---
schema_version: 1
id: DBKB-DARCH-0001
title: Data Architecture Overview
type: overview
primary_domain: data-architecture
secondary_domains: [architecture, governance]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [togaf, dcat]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-META-0001]
related: []
aliases: [enterprise data architecture]
search_keywords: [data architecture, domain, platform, governance, lifecycle]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-DARCH-0001]
source_ids: [SRC-000092, SRC-000093, SRC-000094]
acceptance_criteria: [Data architecture scope, domains, principles, governance and evolution are introduced]
---
# Data Architecture Overview

Data architecture összeköti a business capability-ket, data domain-eket, application-eket, platformokat és governance kontrollokat. A jó target state nem egyetlen diagram: tartalmaz ownershipet, interfaces-t, non-functional requirementeket, lifecycle-t és transition plan-t.

A platform, data product és catalog külön concern; a DCAT-szerű vocabulary segíti az interoperabilitást, de nem helyettesíti a helyi operating modelt. Architecture decision csak explicit trade-off, evidence és review után legyen baseline.

## Források
- [The Open Group TOGAF Standard](https://pubs.opengroup.org/togaf-standard/)
- [W3C DCAT](https://www.w3.org/TR/vocab-dcat-3/)
- [AWS Data Mesh Guidance](https://docs.aws.amazon.com/prescriptive-guidance/latest/modern-data-architectures/data-mesh.html)
