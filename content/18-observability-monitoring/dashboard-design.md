---
schema_version: 1
id: DBKB-OBS-0016
title: Dashboard Design
type: playbook
primary_domain: observability
secondary_domains: [operations]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [prometheus, opentelemetry]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-OBS-0006]
related: []
aliases: [database monitoring dashboard]
search_keywords: [dashboard, drilldown, service view, saturation]
risk: caution
version_sensitive: false
review_cycle: 6m
research_packages: [RP-OBS-0001]
source_ids: [SRC-000055, SRC-000056]
acceptance_criteria: [Audience, hierarchy, drilldown and freshness are addressed]
---
# Dashboard Design

Dashboard hierarchy legyen service overview → SLO/error budget → database health → query/lock/storage drilldown. Panelhez unit, aggregation, time window, source, owner és freshness tartozzon; dashboard ne legyen alert rule-ok nélküli screenshot-gyűjtemény.

## Források
- [OpenTelemetry Documentation](https://opentelemetry.io/docs/)
- [Prometheus Documentation](https://prometheus.io/docs/)
