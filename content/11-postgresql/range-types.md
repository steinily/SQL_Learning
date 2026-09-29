---
schema_version: 1
id: DBKB-PG-0012
title: Range Types
type: technology
primary_domain: postgresql
secondary_domains: [data-modeling]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-PG-0009]
related: [DBKB-PG-0011]
aliases: [range, multirange]
search_keywords: [range type, exclusion constraint, tstzrange]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-PG-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Bound inclusivity, empty range és exclusion use-case-et ad]
---
# Range Types

Range type lower/upper boundokat és inclusivityt reprezentál, például időintervallumot. Üzleti overlap és adjacency szabályoknál exclusion constraint lehet releváns; bound és timezone semantics legyen explicit.

## Források
- [PostgreSQL 18 — Range Types](https://www.postgresql.org/docs/18/rangetypes.html)
