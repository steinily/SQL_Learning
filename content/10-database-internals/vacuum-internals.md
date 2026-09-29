---
schema_version: 1
id: DBKB-INT-0011
title: Vacuum Internals
type: technology
primary_domain: database-internals
secondary_domains: [operations]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-INT-0009, DBKB-INT-0010]
related: [DBKB-INT-0012, DBKB-INT-0015]
aliases: [autovacuum internals]
search_keywords: [vacuum, autovacuum, dead tuples, wraparound]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-INT-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Vacuum cleanup, visibility és statistics szerepét megkülönbözteti]
---
# Vacuum Internals

Vacuum eltávolítja a már nem látható tuple versioneket, frissíti visibility metadata-t és segít a transaction ID health fenntartásában. Vacuum nem feltétlenül adja vissza azonnal a fájlméretet OS szinten; bloat remediation külön folyamat.

## Források
- [PostgreSQL 18 — Routine Vacuuming](https://www.postgresql.org/docs/18/routine-vacuuming.html)
