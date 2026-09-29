---
schema_version: 1
id: DBKB-OBS-0005
title: Prometheus Metrics for Databases
type: technology
primary_domain: observability
secondary_domains: [metrics]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [prometheus, postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-OBS-0003]
related: []
aliases: [Prometheus database exporter]
search_keywords: [Prometheus, exporter, scrape, labels, recording rule]
risk: caution
version_sensitive: true
review_cycle: 6m
research_packages: [RP-OBS-0001]
source_ids: [SRC-000056]
acceptance_criteria: [Metric model, scrape and label risks are explained]
---
# Prometheus Metrics for Databases

Prometheus scrape és exporter segítségével database counters és gauges gyűjthetők. A label cardinality-t kontrolláld: query text, user vagy unbounded identifier labelként való használata storage és query cost növekedést okozhat; recording rule-okkal stabil aggregációt alakíts ki.

## Források
- [Prometheus Documentation](https://prometheus.io/docs/)
