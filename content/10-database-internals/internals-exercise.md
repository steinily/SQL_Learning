---
schema_version: 1
id: DBKB-INT-0025
title: Internals Exercise
type: exercise
primary_domain: database-internals
secondary_domains: [practice]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-INT-0011, DBKB-INT-0016, DBKB-INT-0022]
related: [DBKB-INT-0024]
aliases: [internals lab]
search_keywords: [WAL exercise, vacuum exercise, catalog exercise]
risk: safe
version_sensitive: true
review_cycle: 12m
research_packages: [RP-INT-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Vacuum/WAL/statistics evidence interpretationt gyakoroltatja]
---
# Internals Exercise

Készíts non-production lab reportot: rögzíts relation size/dead tuple és planner statistics állapotot, futtass kontrollált `VACUUM (ANALYZE)` műveletet, majd hasonlítsd össze a plan és catalog evidence-et. A result engine/version és dataset scope-hoz kötött.

## Források
- [PostgreSQL 18 — Routine Vacuuming](https://www.postgresql.org/docs/18/routine-vacuuming.html)
