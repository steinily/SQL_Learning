---
schema_version: 1
id: DBKB-REC-0054
title: Security Incident Playbook
type: playbook
primary_domain: recipes
secondary_domains: [security, operations]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-REC-0053]
related: [DBKB-SEC-0001]
aliases: [database security incident]
search_keywords: [credential leak, unauthorized access, exfiltration, containment, rotation]
risk: security-sensitive
version_sensitive: false
review_cycle: 6m
research_packages: [RP-RECIPES-0001]
source_ids: [SRC-000001]
acceptance_criteria: [Security incident identify, contain, preserve, rotate, recover and review steps are defined]
---
# Security Incident Playbook

Identify scope: principal, resource, action, time, data classification, audit evidence és possible exfiltration. Contain by revoke/isolate/rotate/fence, preserve logs/snapshots, and coordinate security/privacy/legal owners; ne töröld a forensic evidence-et.

Recovery után negative access test, credential/key rotation, vulnerable path closure, consumer notification és retention/legal hold check kell. Root cause és follow-up action csak preserved evidence alapján álljon.

## Forrás
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
