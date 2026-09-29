---
schema_version: 1
id: DBKB-META-0007
title: Technical Lineage
type: technology
primary_domain: lineage
secondary_domains: [metadata]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [openlineage, datahub, apache-spark]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-META-0006]
related: []
aliases: [technical data lineage]
search_keywords: [technical lineage, upstream, downstream, dataset, column lineage]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-META-0001]
source_ids: [SRC-000080, SRC-000082]
acceptance_criteria: [Technical lineage identity, edges, facets and freshness are explained]
---
# Technical Lineage

Technical lineage job/run/dataset edgesből, input/output relationből, schema/column facetből és execution contextből épül. Stable dataset identity, namespace, environment, version, event time és source coverage nélkül graph pontatlan vagy nem összehasonlítható.

## Források
- [OpenLineage Documentation](https://openlineage.io/docs/)
- [DataHub Documentation](https://docs.datahub.com/)
