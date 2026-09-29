---
schema_version: 1
id: DBKB-CLOUD-0002
title: Managed Storage and Compute
type: concept
primary_domain: cloud-data-platforms
secondary_domains: [architecture, performance]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [aws-data-platform, google-bigquery, snowflake]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-CLOUD-0001]
related: [DBKB-CLOUD-0008]
aliases: [separated storage compute]
search_keywords: [managed storage, compute warehouse, autoscaling, quota, workload isolation]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-CLOUD-0001]
source_ids: [SRC-000098, SRC-000099, SRC-000100]
acceptance_criteria: [Storage/compute separation, workload isolation, scaling, quota and cost controls are explained]
---
# Managed Storage and Compute

Managed platformon a storage és compute separation, warehouse/cluster sizing, autoscaling és workload isolation külön döntés lehet. A concurrency, queue, reservation, spill, cache és quota behavior-t mért workloadtal validáld.

Service limit, region, SLA és billing unit legyen a capacity plan része. Autoscaling nem garantálja a költség vagy latency SLO-t; budget alert, quota guard, cancellation és noisy-neighbor isolation kell.

## Források
- [AWS Analytics Documentation](https://docs.aws.amazon.com/analytics/)
- [Google Cloud BigQuery Documentation](https://cloud.google.com/bigquery/docs)
- [Snowflake Documentation](https://docs.snowflake.com/)
