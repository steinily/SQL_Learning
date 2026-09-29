---
schema_version: 1
id: DBKB-DARCH-0010
title: Data Architecture Governance
type: playbook
primary_domain: data-architecture
secondary_domains: [governance, security]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [togaf, dcat]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-DARCH-0009]
related: [DBKB-DARCH-0005]
aliases: [architecture review board]
search_keywords: [architecture governance, review, exception, baseline, compliance]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-DARCH-0001]
source_ids: [SRC-000092, SRC-000093, SRC-000094]
acceptance_criteria: [Review gates, decision rights, exceptions, standards and evidence are actionable]
---
# Data Architecture Governance

Governance operating modelben legyen decision authority, architecture review gate, standard/pattern catalog, exception expiry, risk acceptance és escalation. A review ne diagram review legyen: contract, ownership, threat, cost, SLO, lifecycle és migration evidence is kell.

Baseline változásához ADR, impact analysis, consumer communication, version/deprecation plan és rollback owner tartozzon. Federated környezetben a central rule-ek csak indokolt minimumot írjanak elő, a local domain döntéseket és audit evidence-et pedig láthatóvá kell tenni.

## Források
- [The Open Group TOGAF Standard](https://pubs.opengroup.org/togaf-standard/)
- [W3C DCAT](https://www.w3.org/TR/vocab-dcat-3/)
- [AWS Data Mesh Guidance](https://docs.aws.amazon.com/prescriptive-guidance/latest/modern-data-architectures/data-mesh.html)
