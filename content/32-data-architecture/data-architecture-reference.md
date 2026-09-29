---
schema_version: 1
id: DBKB-DARCH-0015
title: Data Architecture Reference
type: reference
primary_domain: data-architecture
secondary_domains: [architecture, governance]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [togaf, dcat, data-mesh]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-DARCH-0014]
related: [DBKB-DARCH-0002, DBKB-DARCH-0010]
aliases: [architecture checklist]
search_keywords: [data architecture checklist, ownership, SLO, contract, ADR]
risk: production-critical
version_sensitive: false
review_cycle: 12m
research_packages: [RP-DARCH-0001]
source_ids: [SRC-000092, SRC-000093, SRC-000094]
acceptance_criteria: [Concise architecture review and go-live checklist is provided]
---
# Data Architecture Reference

Review checklist: business capability és domain boundary; owner/steward; data product contract; source/lineage; quality/freshness SLO; security classification/access; platform quota/isolation; lifecycle/retention; cost; observability; ADR/exception; migration/rollback; consumer communication.

Go-live csak akkor: contract published, catalog identity stable, quality/security tests PASS, restore/rollback evidence exists, alert/runbook owner assigned és deprecation policy communicated.

## Források
- [The Open Group TOGAF Standard](https://pubs.opengroup.org/togaf-standard/)
- [W3C DCAT](https://www.w3.org/TR/vocab-dcat-3/)
- [AWS Data Mesh Guidance](https://docs.aws.amazon.com/prescriptive-guidance/latest/modern-data-architectures/data-mesh.html)
