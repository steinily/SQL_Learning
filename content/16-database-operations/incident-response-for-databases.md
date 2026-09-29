---
schema_version: 1
id: DBKB-OPS-0015
title: Incident Response for Databases
type: playbook
primary_domain: database-operations
secondary_domains: [reliability]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-OPS-0016]
related: []
aliases: [DB incident response]
search_keywords: [database incident, triage, containment, postmortem]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-OPS-0001]
source_ids: [SRC-000049]
acceptance_criteria: [Triage, containment, recovery and learning loop are described]
---
# Incident Response for Databases

Incident response-ben először scope-old a blast radius-t és védd az evidence-et. Triage, containment, recovery, communication és post-incident review külön lépés legyen; production adat módosítása előtt legyen explicit approval és rollback vagy restore plan.

## Források
- [PostgreSQL — Monitoring Database Activity](https://www.postgresql.org/docs/current/monitoring.html)
