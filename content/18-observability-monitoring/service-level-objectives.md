---
schema_version: 1
id: DBKB-OBS-0007
title: Service Level Objectives
type: concept
primary_domain: observability
secondary_domains: [reliability, governance]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql, prometheus]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-OBS-0006]
related: []
aliases: [database SLO]
search_keywords: [SLO, SLA, error budget, availability, latency objective]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-OBS-0001]
source_ids: [SRC-000056]
acceptance_criteria: [SLO indicators, windows and error budget decisions are specified]
---
# Service Level Objectives

Database SLO a user-relevant service indicatorre épüljön, például successful transaction availability, bounded latency vagy freshness, ne pusztán process uptime-ra. Dokumentáld targetet, measurement window-t, exclusions-t, error budget policy-t és owner döntéseit.

## Források
- [Prometheus Documentation](https://prometheus.io/docs/)
