---
schema_version: 1
id: DBKB-SQ-0004
title: SQLite Typing
type: concept
primary_domain: sqlite
secondary_domains: [data-modeling]
levels: [intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [sqlite]
sql_dialects: [sqlite]
scope: vendor-specific
prerequisites: [DBKB-SQ-0001]
related: [DBKB-SQ-0013]
aliases: [dynamic typing, type affinity]
search_keywords: [SQLite typing, type affinity, storage class]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-SQ-0001]
source_ids: [SRC-000048]
acceptance_criteria: [Storage class, affinity, conversion és STRICT table caveat-et adja]
---
# SQLite Typing

SQLite dynamic type system storage classes és column affinity alapján működik, ezért declared type nem mindig kényszerít rigid storage type-ot. Type-sensitive application contractnál validation, explicit cast vagy STRICT table használata szükséges.

## Források
- [SQLite — Datatypes In SQLite](https://www.sqlite.org/datatype3.html)
