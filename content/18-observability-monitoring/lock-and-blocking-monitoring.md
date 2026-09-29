---
schema_version: 1
id: DBKB-OBS-0011
title: Lock and Blocking Monitoring
type: technology
primary_domain: observability
secondary_domains: [concurrency]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-OBS-0003]
related: []
aliases: [database blocking telemetry]
search_keywords: [lock wait, blocking, deadlock, wait graph]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-OBS-0001]
source_ids: [SRC-000054]
acceptance_criteria: [Blocking signal, causality and safe response are described]
---
# Lock and Blocking Monitoring

Blocking telemetry kapcsolja össze blocker és waiter sessiont, lock type-ot, durationt, transaction age-et és query contextet. A remediation ne automatikus kill legyen: előbb ellenőrizd transaction intentet, business impactet, timeout policy-t és a safe termination lehetőségét.

## Források
- [PostgreSQL — Monitoring Database Activity](https://www.postgresql.org/docs/current/monitoring.html)
