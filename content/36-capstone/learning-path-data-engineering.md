---
schema_version: 1
id: DBKB-CAP-0076
title: Learning Path Data Engineering
type: learning-path
primary_domain: capstone
secondary_domains: [data-engineering, pipelines]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, apache-kafka, openmetadata]
sql_dialects: [postgresql]
scope: cross-vendor
prerequisites: [DBKB-CAP-0075]
related: [DBKB-CAP-0057]
aliases: [data engineering path]
search_keywords: [data engineering learning path, pipeline, batch, quality, lineage]
risk: production-critical
version_sensitive: false
review_cycle: 12m
research_packages: [RP-CAPSTONE-0001]
source_ids: [SRC-000001, SRC-000080]
acceptance_criteria: [Ordered data engineering path with pipeline, quality, lineage and recovery milestones]
---
# Learning Path Data Engineering

Sorrend: modeling/SQL → batch pipeline → schema/contract → quality/quarantine → lineage/metadata → idempotent replay/backfill → data engineering exercise/case/reference.

Exit criteria: checkpoint/watermark, quality/SLO, lineage, reconciliation, failure recovery és owner/runbook evidence.

## Források
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [OpenLineage Documentation](https://openlineage.io/docs/)
