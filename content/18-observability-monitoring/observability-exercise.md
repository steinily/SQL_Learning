---
schema_version: 1
id: DBKB-OBS-0022
title: Observability Exercise
type: exercise
primary_domain: observability
secondary_domains: [validation]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [opentelemetry, prometheus, postgresql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-OBS-0021]
related: []
aliases: [observability tabletop exercise]
search_keywords: [observability exercise, alert drill, telemetry gap]
risk: caution
version_sensitive: false
review_cycle: 6m
research_packages: [RP-OBS-0001]
source_ids: [SRC-000055, SRC-000056]
acceptance_criteria: [Exercise defines evidence without claiming unexecuted results]
---
# Observability Exercise

Tervezd meg egy database latency spike, collector outage és replication freshness breach gyakorlatát. Készíts alert timeline-t, dashboard evidence-et, native fallback query-ket, cardinality/cost döntést, incident communicationt és recovery verificationt; execution-verified csak tényleges futtatás után adható.

## Források
- [OpenTelemetry Documentation](https://opentelemetry.io/docs/)
- [Prometheus Documentation](https://prometheus.io/docs/)
