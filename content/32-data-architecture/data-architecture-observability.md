---
schema_version: 1
id: DBKB-DARCH-0012
title: Data Architecture Observability
type: technology
primary_domain: data-architecture
secondary_domains: [observability, operations]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [dcat]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-DARCH-0011]
related: [DBKB-OBS-0001, DBKB-META-0009]
aliases: [architecture telemetry]
search_keywords: [data architecture observability, freshness, lineage, SLO, cost]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-DARCH-0001]
source_ids: [SRC-000092, SRC-000093, SRC-000094]
acceptance_criteria: [Platform, data product and architecture health signals with ownership are defined]
---
# Data Architecture Observability

Architecture-level telemetry kapcsolja össze a platform health-et és a data product SLO-t: freshness, completeness, schema compatibility, lineage freshness, access latency/error, cost, capacity és incident rate.

Dataset/distribution/service identity legyen trace-elhető a pipeline run, storage, consumer query és change/ADR felé. Alert csak ownerrel, thresholdtal, durationnel és runbookkal legyen productionben; dashboard aggregate ne fedje el a domain vagy tenant outliert.

## Források
- [W3C DCAT](https://www.w3.org/TR/vocab-dcat-3/)
- [AWS Data Mesh Guidance](https://docs.aws.amazon.com/prescriptive-guidance/latest/modern-data-architectures/data-mesh.html)
