---
schema_version: 1
id: DBKB-REC-0024
title: Architecture Recipes
type: playbook
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
prerequisites: [DBKB-REC-0023]
related: [DBKB-DARCH-0001]
aliases: [architecture decision recipe]
search_keywords: [ADR, architecture review, boundary, data product, transition]
risk: production-critical
version_sensitive: false
review_cycle: 12m
research_packages: [RP-RECIPES-0001]
source_ids: [SRC-000092, SRC-000093, SRC-000094]
acceptance_criteria: [Architecture context, options, decision, controls, transition and review evidence are actionable]
---
# Architecture Recipes

Architecture recipe: context/constraints, capability and data boundaries, NFR/SLO, options, trade-off, chosen decision, security/cost impact, owner, transition, rollback, review date és supersession link.

Review gate ne csak diagramot nézzen: interface, ownership, lifecycle, lineage, policy, observability és dependency evidence kell. Exception expiry nélkül a baseline driftje rejtve marad.

## Források
- [The Open Group TOGAF Standard](https://pubs.opengroup.org/togaf-standard/)
- [W3C DCAT](https://www.w3.org/TR/vocab-dcat-3/)
- [AWS Data Mesh Guidance](https://docs.aws.amazon.com/prescriptive-guidance/latest/modern-data-architectures/data-mesh.html)
