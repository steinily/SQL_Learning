---
schema_version: 1
id: DBKB-INT-0013
title: Free Space Map
type: technology
primary_domain: database-internals
secondary_domains: [storage]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-INT-0004]
related: [DBKB-INT-0011]
aliases: [FSM]
search_keywords: [free space map, page free space, tuple placement]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-INT-0001]
source_ids: [SRC-000014]
acceptance_criteria: [FSM célját és page allocation szerepét adja]
---
# Free Space Map

Free Space Map relationenként a page-ek becsült szabad helyét tartja nyilván, hogy új tuple vagy tuple version számára gyorsan található legyen alkalmas page. Az estimate nem application-visible kapacitásgarancia.

## Források
- [PostgreSQL 18 — Free Space Map](https://www.postgresql.org/docs/18/storage-fsm.html)
