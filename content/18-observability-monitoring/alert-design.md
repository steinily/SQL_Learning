---
schema_version: 1
id: DBKB-OBS-0008
title: Alert Design
type: playbook
primary_domain: observability
secondary_domains: [reliability]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [prometheus, postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-OBS-0007]
related: []
aliases: [database alert rules]
search_keywords: [alert rule, threshold, burn rate, actionable alert]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-OBS-0001]
source_ids: [SRC-000056]
acceptance_criteria: [Alert condition, severity, owner, runbook and reset behavior are defined]
---
# Alert Design

Alert csak actionable condition legyen: explicit signal, window, severity, owner, runbook link és notification route tartozzon hozzá. Preferáld a sustained symptom vagy SLO burn alertet a noisy instant threshold helyett, és teszteld firing valamint recovery állapotban is.

## Források
- [Prometheus — Alerting Rules](https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/)
