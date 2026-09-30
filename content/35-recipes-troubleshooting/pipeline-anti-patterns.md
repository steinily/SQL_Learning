---
schema_version: 1
id: DBKB-REC-0046
title: Pipeline Anti-Patterns
type: error
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
prerequisites: [DBKB-REC-0045]
related: [DBKB-INTG-0001]
aliases: [pipeline mistakes]
search_keywords: [pipeline anti-pattern, infinite retry, no watermark, partial publish, hidden failure]
risk: production-critical
version_sensitive: false
review_cycle: 12m
research_packages: [RP-RECIPES-0001]
source_ids: [SRC-000080, SRC-000087]
acceptance_criteria: [Pipeline anti-patterns include detection, containment and recovery controls]
---
# Pipeline Anti-Patterns

Anti-pattern az infinite retry, watermark/checkpoint nélkül replay, non-idempotent fan-out, partial output publish, schema validation nélküli ingest, dropped dead-letter és success csak process exit alapján.

Detectáld input/output count, lag, run state, retries, quarantine, lineage freshness és reconciliation trend alapján. Remediation: bounded retry, durable checkpoint, quarantine, contract gate, atomic publish és post-run business validation.

## Források
- [OpenLineage Documentation](https://openlineage.io/docs/)
- [Apache Kafka Documentation](https://kafka.apache.org/documentation/)
