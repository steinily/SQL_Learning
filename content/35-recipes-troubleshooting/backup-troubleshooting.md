---
schema_version: 1
id: DBKB-REC-0032
title: Backup Troubleshooting
type: troubleshooting
primary_domain: recipes
secondary_domains: [disaster-recovery, operations]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql, sqlite]
sql_dialects: [postgresql, tsql, mysql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-REC-0031]
related: [DBKB-DR-0001]
aliases: [backup failure runbook]
search_keywords: [backup failure, restore, checksum, retention, RPO]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-RECIPES-0001]
source_ids: [SRC-000001]
acceptance_criteria: [Failed backup, incomplete restore, retention and evidence diagnosis are actionable]
---
# Backup Troubleshooting

Ellenőrizd a backup job status/timestamp, consistency boundary-t, source connectivityt, disk/object quota-t, encryption/key availabilityt és retention policy-t. „Job succeeded” után is ellenőrizd artifact size/checksum és catalog registration értékét.

Restore hiba esetén izoláld a targetet, preserve-öld a backup evidence-et, azonosítsd a missing log/metadata/index problémát és csak bounded replay-t futtass. RPO/RTO breach legyen incident, ownerrel és communicationnel.

## Forrás
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
