---
schema_version: 1
id: DBKB-IDX-0025
title: Indexing Decision Record
type: playbook
primary_domain: indexing
secondary_domains: [governance]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: cross-vendor
prerequisites: [DBKB-IDX-0023]
related: [DBKB-IDX-0024]
aliases: [index ADR]
search_keywords: [index decision record, index ADR, tuning record]
risk: production-critical
version_sensitive: false
review_cycle: 12m
research_packages: [RP-IDX-0001]
source_ids: [SRC-000014]
acceptance_criteria: ["Index decision record mezőit: context, evidence, impact, rollback, owner"]
---
# Indexing Decision Record

Rögzítsd a contextet, érintett queryt és workloadot, a választott index type/column ordert, az előtte-utána evidence-et, a write/storage impactot, rollbacket, owner-t és review date-et. Így a tuning döntés később auditálható.

## Források
- [PostgreSQL 18 — Indexes](https://www.postgresql.org/docs/18/indexes.html)
