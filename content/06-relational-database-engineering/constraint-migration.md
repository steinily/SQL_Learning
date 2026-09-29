---
schema_version: 1
id: DBKB-RDBE-0016
title: Constraint Migration
type: playbook
primary_domain: relational-database-engineering
secondary_domains: [data-quality, migrations]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-RDBE-0003, DBKB-MODL-0023]
related: [DBKB-RDBE-0015]
aliases: [constraint rollout]
search_keywords: [constraint, backfill, validate, foreign key, not null]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-RDBE-0001]
source_ids: [SRC-000009]
acceptance_criteria: [Dirty data discovery/backfill/validation lépéseket ad, Constraint enforcement timingot scope-olja]
---
# Constraint Migration

Új constraint rolloutja három fázis: profile és violation inventory; repair/backfill; enforcement és
postcondition. Existing dirty data mellett közvetlen `NOT NULL`, UNIQUE vagy FK addition production
failuret okozhat.

Backfill idempotens, chunkolt és auditált legyen. Concurrent writers ugyanabban a windowban új violationt
hozhatnak; átmeneti dual validation vagy write gate szükséges. Constraint mode és validation syntax
engine-specific.

## Források

- [PostgreSQL 18 — Constraints](https://www.postgresql.org/docs/18/ddl-constraints.html)
