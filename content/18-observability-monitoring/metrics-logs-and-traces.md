---
schema_version: 1
id: DBKB-OBS-0002
title: Metrics Logs and Traces
type: concept
primary_domain: observability
secondary_domains: [architecture]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [opentelemetry]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-OBS-0001]
related: []
aliases: [observability signals]
search_keywords: [metrics, logs, traces, correlation, context]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-OBS-0001]
source_ids: [SRC-000055]
acceptance_criteria: [Signal semantics, correlation and trade-offs are explained]
---
# Metrics Logs and Traces

Metrics trendet és aggregált state-et, logs eseményeket és contextet, traces pedig request path és latency breakdown-t adnak. Correlationhez consistent resource/service/trace context kell; signal duplication, high cardinality és sampling korlátait dokumentáld.

## Források
- [OpenTelemetry Documentation](https://opentelemetry.io/docs/)
