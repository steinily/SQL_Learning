---
schema_version: 1
id: DBKB-DQ-0009
title: Timeliness and Freshness
type: technology
primary_domain: data-quality
secondary_domains: [reliability, observability]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [great-expectations, dbt]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-DQ-0008]
related: []
aliases: [data freshness]
search_keywords: [timeliness, freshness, watermark, lateness, SLA]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-DQ-0001]
source_ids: [SRC-000077, SRC-000078]
acceptance_criteria: [Freshness indicator, expected window, late data and breach response are defined]
---
# Timeliness and Freshness

Timeliness/freshness source event time, ingestion time, processing completion és consumer availability alapján mérendő. Expected window, watermark, late-arrival grace, timezone, last-known-good state és breach escalation legyen explicit; a pipeline run timestamp önmagában nem freshness proof.

## Források
- [Great Expectations Documentation](https://docs.greatexpectations.io/docs/)
- [dbt — Data Tests](https://docs.getdbt.com/docs/build/tests)
