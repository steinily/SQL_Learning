---
schema_version: 1
id: DBKB-CLOUD-0001
title: Cloud Data Platforms Overview
type: overview
primary_domain: cloud-data-platforms
secondary_domains: [architecture, operations]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [aws-data-platform, google-bigquery, snowflake]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-DARCH-0006]
related: []
aliases: [cloud analytics platform]
search_keywords: [cloud data platform, managed service, storage, compute, governance]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-CLOUD-0001]
source_ids: [SRC-000098, SRC-000099, SRC-000100]
acceptance_criteria: [Managed storage, compute, governance, security, cost and portability tradeoffs are introduced]
---
# Cloud Data Platforms Overview

Cloud data platform managed storage, compute, catalog/governance, security, networking, observability és FinOps capability-k együttese. A managed control plane csökkentheti az operational burden-t, de quota, region, IAM, egress, cost és provider lock-in továbbra is architecture decision.

AWS, BigQuery és Snowflake hasonló capability-ket különböző service és pricing semantics-szel ad; feature parityt nem feltételezz. Target architecturehez workload, data residency, SLO, exit path és tényleges account constraints kell.

## Források
- [AWS Analytics Documentation](https://docs.aws.amazon.com/analytics/)
- [Google Cloud BigQuery Documentation](https://cloud.google.com/bigquery/docs)
- [Snowflake Documentation](https://docs.snowflake.com/)
