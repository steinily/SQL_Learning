---
schema_version: 1
id: DBKB-INT-0012
title: Visibility Map
type: technology
primary_domain: database-internals
secondary_domains: [performance]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-INT-0011]
related: [DBKB-IDX-0006, DBKB-PERF-0007]
aliases: [visibility map bits]
search_keywords: [visibility map, all-visible, index-only scan]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-INT-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Visibility map és index-only scan kapcsolatát magyarázza]
---
# Visibility Map

Visibility map page-szinten jelzi, hogy minden tuple minden active transaction számára látható-e. Ez támogatja az index-only scan heap fetch elkerülését; update és vacuum után a bit állapota változhat.

## Források
- [PostgreSQL 18 — Visibility Map](https://www.postgresql.org/docs/18/storage-vm.html)
