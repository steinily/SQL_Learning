---
schema_version: 1
id: DBKB-REC-0051
title: Architecture Anti-Patterns
type: error
primary_domain: recipes
secondary_domains: [data-architecture, governance]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [togaf, dcat]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-REC-0050]
related: [DBKB-DARCH-0016]
aliases: [data architecture mistakes]
search_keywords: [big bang, diagram theater, central bottleneck, no ownership, exception drift]
risk: production-critical
version_sensitive: false
review_cycle: 12m
research_packages: [RP-RECIPES-0001]
source_ids: [SRC-000092, SRC-000093, SRC-000094]
acceptance_criteria: [Architecture anti-patterns include detection and governance remediation]
---
# Architecture Anti-Patterns

Anti-pattern a big-bang target transition plan nélkül, diagram-only review, central platform owner nélkül, shared data domain contract nélkül, catalog lineage nélkül és non-expiring exception.

Detectáld decision/ownership/consumer/SLO/lineage coverage és exception age metric alapján. Remediation ADR, bounded transition, domain accountability, contract, evidence, review gate és expiry legyen.

## Források
- [The Open Group TOGAF Standard](https://pubs.opengroup.org/togaf-standard/)
- [W3C DCAT](https://www.w3.org/TR/vocab-dcat-3/)
- [AWS Data Mesh Guidance](https://docs.aws.amazon.com/prescriptive-guidance/latest/modern-data-architectures/data-mesh.html)
