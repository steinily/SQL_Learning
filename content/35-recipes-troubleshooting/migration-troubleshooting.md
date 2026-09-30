---
schema_version: 1
id: DBKB-REC-0033
title: Migration Troubleshooting
type: troubleshooting
primary_domain: recipes
secondary_domains: [migration, operations]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql, sqlite]
sql_dialects: [postgresql, tsql, mysql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-REC-0032]
related: [DBKB-MIG-0001]
aliases: [migration incident runbook]
search_keywords: [migration failure, backfill drift, cutover, dual write, rollback]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-RECIPES-0001]
source_ids: [SRC-000001]
acceptance_criteria: [Schema, data, lag, drift, cutover and rollback diagnosis are covered]
---
# Migration Troubleshooting

Classify the incident: schema incompatibility, failed DDL, backfill lag, dual-write drift, checksum/count mismatch, lock/timeout or consumer break. Capture source/target revision, watermark, row counts, errors and last consistent checkpoint.

Containment: stop cutover, freeze destructive cleanup, quarantine drift and preserve rollback source. Resume only after idempotent correction, representative reconciliation and consumer sign-off; do not hide mismatch with blind overwrite.

## Forrás
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
