---
schema_version: 1
id: DBKB-DR-0009
title: Backup Retention and Legal Hold
type: playbook
primary_domain: backup
secondary_domains: [governance, privacy]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-DR-0008]
related: []
aliases: [backup retention policy]
search_keywords: [backup retention, legal hold, deletion, archive]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-DR-0001]
source_ids: [SRC-000064]
acceptance_criteria: [Retention schedule, legal hold, privacy and expiry evidence are defined]
---
# Backup Retention and Legal Hold

Retention schedule a RPO, recovery horizon, legal/regulatory requirement, privacy purpose és storage cost együttese. Legal hold felfüggesztheti az expiry-t, de owner, scope, start/end evidence és release workflow kell; backup expiry a primary deletion policy-tól külön is kezelendő.

## Források
- [NIST SP 800-34 Rev. 1](https://csrc.nist.gov/publications/detail/sp/800-34/rev-1/final)
