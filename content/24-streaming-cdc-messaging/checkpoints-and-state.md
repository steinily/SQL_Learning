---
schema_version: 1
id: DBKB-STREAM-0008
title: Checkpoints and State
type: technology
primary_domain: streaming
secondary_domains: [reliability]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [apache-flink]
sql_dialects: [postgresql, tsql, mysql]
scope: vendor-specific
prerequisites: [DBKB-STREAM-0007]
related: []
aliases: [stream checkpoint]
search_keywords: [checkpoint, state snapshot, recovery, savepoint, exactly once]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-STREAM-0001]
source_ids: [SRC-000072]
acceptance_criteria: [Checkpoint, savepoint, state recovery and sink coordination are explained]
---
# Checkpoints and State

Checkpoint a source position, operator state és processing progress consistent snapshotját rögzítheti; savepoint controlled upgrade/migration artifact lehet. Interval, timeout, alignment, state backend, externalized retention és sink commit behavior target Flink deploymenten validálandó.

## Források
- [Apache Flink Documentation](https://nightlies.apache.org/flink/flink-docs-stable/)
