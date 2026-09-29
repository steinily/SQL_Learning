---
schema_version: 1
id: DBKB-IDX-0023
title: Index Review Checklist
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
prerequisites: [DBKB-IDX-0022]
related: [DBKB-IDX-0025]
aliases: [index review]
search_keywords: [index checklist, index design review]
risk: production-critical
version_sensitive: false
review_cycle: 12m
research_packages: [RP-IDX-0001]
source_ids: [SRC-000014]
acceptance_criteria: ["Review steps: workload, plan, write cost, ownership, rollback"]
---
# Index Review Checklist

Review sorrend: query és workload evidence; predicate/order illeszkedés; cardinality/statistics; write és storage cost; concurrency/maintenance; monitoring; rollback és owner. A jóváhagyás legyen reproducible `EXPLAIN` és mérési artefacttal.

## Források
- [PostgreSQL 18 — Using EXPLAIN](https://www.postgresql.org/docs/18/using-explain.html)
