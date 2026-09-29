---
schema_version: 1
id: DBKB-MIG-0005
title: Backward Compatible Changes
type: concept
primary_domain: migration
secondary_domains: [data-contracts]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-MIG-0004]
related: []
aliases: [compatible schema change]
search_keywords: [backward compatibility, additive change, nullable column, consumer]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-MIG-0001]
source_ids: [SRC-000060, SRC-000061, SRC-000062]
acceptance_criteria: [Consumer compatibility and breaking-change detection are defined]
---
# Backward Compatible Changes

Backward-compatible change-nél régi consumer és régi query path tovább működik az új schema mellett. Additive nullable field, dual-read vagy compatibility view csak target engine semantics, default cost, index impact és consumer contract tesztje után tekinthető safe-nek.

## Források
- [PostgreSQL — SQL Commands](https://www.postgresql.org/docs/current/sql-commands.html)
