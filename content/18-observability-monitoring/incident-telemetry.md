---
schema_version: 1
id: DBKB-OBS-0017
title: Incident Telemetry
type: playbook
primary_domain: observability
secondary_domains: [incident-management]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [opentelemetry, prometheus, postgresql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-OBS-0008]
related: []
aliases: [incident observability]
search_keywords: [incident timeline, telemetry snapshot, correlation]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-OBS-0001]
source_ids: [SRC-000054, SRC-000055]
acceptance_criteria: [Incident evidence capture and timeline correlation are defined]
---
# Incident Telemetry

Incident alatt capture-eld a relevant metric windowt, logs/traces correlationt, database activity snapshotot, deploy/config change-et és user impactot. Preserve-eld az eredeti evidence-et, jelöld a query time zone-t és collection gap-et, majd a timeline-t hypothesis és verified fact szerint különítsd el.

## Források
- [OpenTelemetry Documentation](https://opentelemetry.io/docs/)
- [PostgreSQL — Monitoring Database Activity](https://www.postgresql.org/docs/current/monitoring.html)
