---
schema_version: 1
id: DBKB-IDX-0007
title: Partial Indexes
type: technology
primary_domain: indexing
secondary_domains: [postgresql]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-IDX-0003]
related: [DBKB-IDX-0008, DBKB-IDX-0022]
aliases: [filtered index predicate]
search_keywords: [partial index, predicate index, filtered rows]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-IDX-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Partial predicate és query implication scopeját bemutatja]
---
# Partial Indexes

Partial index csak a megadott predicate-nek megfelelő sorokat indexeli, csökkentve a méretet és write costot, ha a workload jól illeszkedik. A planner csak akkor használhatja, ha a query feltétele a predicate-tel összeegyeztethető.

## Források
- [PostgreSQL 18 — Partial Indexes](https://www.postgresql.org/docs/18/indexes-partial.html)
