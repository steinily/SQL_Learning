---
schema_version: 1
id: DBKB-WH-0015
title: Metrics and Measures
type: concept
primary_domain: data-warehouse
secondary_domains: [governance, analytics]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [apache-spark, parquet]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-WH-0014]
related: []
aliases: [warehouse metrics]
search_keywords: [metric, measure, KPI, denominator, grain, definition]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-WH-0001]
source_ids: [SRC-000066]
acceptance_criteria: [Metric definition, grain, denominator, owner and tests are specified]
---
# Metrics and Measures

Metric contract tartalmazza a business definitiont, grain-t, numerator/denominator-t, filtert, time zone-t, null/unknown policy-t, ownert, versiont és testet. KPI név önmagában nem elég: ugyanazon measure eltérő populationnel vagy snapshot date-tel más eredményt ad.

## Források
- [Apache Spark Documentation](https://spark.apache.org/docs/latest/)
