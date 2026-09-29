---
schema_version: 1
id: DBKB-DARCH-0005
title: Architecture Decision Records
type: playbook
primary_domain: data-architecture
secondary_domains: [governance, operations]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [togaf]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-DARCH-0004]
related: [DBKB-DARCH-0010]
aliases: [ADR]
search_keywords: [architecture decision record, context, options, tradeoff, superseded]
risk: production-critical
version_sensitive: false
review_cycle: 12m
research_packages: [RP-DARCH-0001]
source_ids: [SRC-000092]
acceptance_criteria: [ADR structure captures context, decision, consequences, evidence and review state]
---
# Architecture Decision Records

ADR minimum: context/problem, constraints, options considered, decision, consequences, security/quality impact, owner, date, evidence, review date és supersession link. A rejected option és annak indoka is fontos, hogy később ne ismételd meg ugyanazt a döntést.

Architecture baseline csak akkor legyen „accepted”, ha a decision authority jóváhagyta és a transition owner ismert. Production evidence, benchmark és execution result külön artifactként hivatkozzon tényleges outputra; ne írj előre állított eredményt.

## Forrás
- [The Open Group TOGAF Standard](https://pubs.opengroup.org/togaf-standard/)
