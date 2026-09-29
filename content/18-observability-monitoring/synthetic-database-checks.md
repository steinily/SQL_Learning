---
schema_version: 1
id: DBKB-OBS-0020
title: Synthetic Database Checks
type: playbook
primary_domain: observability
secondary_domains: [reliability]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql, opentelemetry]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-OBS-0007]
related: []
aliases: [synthetic transaction check]
search_keywords: [synthetic check, canary query, readiness, smoke test]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-OBS-0001]
source_ids: [SRC-000055]
acceptance_criteria: [Safe synthetic path, data isolation and alert semantics are defined]
---
# Synthetic Database Checks

Synthetic check a real user path kis, controlled és reversible változatát futtatja. Használj dedicated test tenant/objectot, bounded timeoutot, deterministic cleanupot és explicit read/write policy-t; a check failuret correlate-eld native health signalokkal, ne tekintsd önmagában root cause-nak.

## Források
- [OpenTelemetry Documentation](https://opentelemetry.io/docs/)
