---
schema_version: 1
id: DBKB-REC-0036
title: Pipeline Troubleshooting
type: troubleshooting
primary_domain: recipes
secondary_domains: [data-integration, operations]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [apache-kafka, openmetadata]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-REC-0035]
related: [DBKB-INTG-0001]
aliases: [data pipeline incident]
search_keywords: [pipeline failure, DAG, lag, retry, quarantine, watermark]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-RECIPES-0001]
source_ids: [SRC-000080, SRC-000087]
acceptance_criteria: [Pipeline stage, watermark, retry, lag, quarantine and reconciliation diagnosis are actionable]
---
# Pipeline Troubleshooting

Trace-eld a pipeline run ID-n keresztül source ingest, transform, quality, publish, catalog és consumer stage-eket. Capture watermark, input/output counts, schema revision, retry count, lag, error class és last successful checkpoint.

Stop-old the fan-out vagy publish stage-et, ha partial output/contract break veszélye van. Replay only from known boundary, idempotent key-jel és bounded scope-pal; végül count/checksum/quality/lineage és consumer freshness validation kell.

## Források
- [OpenLineage Documentation](https://openlineage.io/docs/)
- [Apache Kafka Documentation](https://kafka.apache.org/documentation/)
