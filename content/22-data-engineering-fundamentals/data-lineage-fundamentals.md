---
schema_version: 1
id: DBKB-DE-0008
title: Data Lineage Fundamentals
type: concept
primary_domain: data-engineering
secondary_domains: [governance, metadata]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [apache-spark, apache-airflow]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-DE-0007]
related: []
aliases: [data lineage]
search_keywords: [lineage, upstream, downstream, impact analysis, provenance]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-DE-0001]
source_ids: [SRC-000066, SRC-000067]
acceptance_criteria: [Technical and business lineage, provenance and impact analysis are defined]
---
# Data Lineage Fundamentals

Lineage source-to-target graphként mutatja az upstream/downstream kapcsolatot, transformationt, ownershipet, freshness-t és schema versiont. Technical lineage önmagában nem business meaning; column-level vagy event-level provenance csak explicit capture és evidence mellett állítható.

## Források
- [Apache Spark Documentation](https://spark.apache.org/docs/latest/)
- [Apache Airflow Documentation](https://airflow.apache.org/docs/)
