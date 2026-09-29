---
schema_version: 1
id: DBKB-INT-0003
title: Pages and Tuples
type: technology
primary_domain: database-internals
secondary_domains: [postgresql]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-INT-0002]
related: [DBKB-INT-0004, DBKB-INT-0014]
aliases: [page layout, tuple layout]
search_keywords: [page, tuple, row storage, block]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-INT-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Page/block, tuple és row version különbségét tisztázza]
---
# Pages and Tuples

PostgreSQL relation files page/block egységekben tárolódnak, a tuple pedig egy row version fizikai reprezentációja. A logical row és fizikai tuple nem azonos, különösen MVCC update és bloat vizsgálatakor.

## Források
- [PostgreSQL 18 — Database Page Layout](https://www.postgresql.org/docs/18/storage-page-layout.html)
