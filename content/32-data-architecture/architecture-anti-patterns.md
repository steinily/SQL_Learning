---
schema_version: 1
id: DBKB-DARCH-0016
title: Architecture Anti-Patterns
type: error
primary_domain: data-architecture
secondary_domains: [governance, operations]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [togaf, dcat, data-mesh]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-DARCH-0015]
related: [DBKB-DARCH-0002, DBKB-DARCH-0010]
aliases: [data architecture mistakes]
search_keywords: [architecture anti-pattern, big bang, central bottleneck, orphan data, diagram theater]
risk: production-critical
version_sensitive: false
review_cycle: 12m
research_packages: [RP-DARCH-0001]
source_ids: [SRC-000092, SRC-000093, SRC-000094]
acceptance_criteria: [Common architecture failure modes include concrete detection and remediation]
---
# Architecture Anti-Patterns

Kerüld a „big bang” target architecture-t transition plan nélkül, a central platform bottlenecket domain ownership nélkül, a diagram-only governance-t evidence nélkül és az implicit data productot contract/SLO nélkül.

További anti-pattern az ownership nélküli shared table, catalog metadata lineage nélkül, security review utólagos hozzáadása, exception expiry hiánya és cloud-specific advice univerzális standardként való kezelése. Minden eltéréshez owner, risk acceptance, expiry és remediation backlog kell.

## Források
- [The Open Group TOGAF Standard](https://pubs.opengroup.org/togaf-standard/)
- [W3C DCAT](https://www.w3.org/TR/vocab-dcat-3/)
- [AWS Data Mesh Guidance](https://docs.aws.amazon.com/prescriptive-guidance/latest/modern-data-architectures/data-mesh.html)
