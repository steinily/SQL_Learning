---
schema_version: 1
id: DBKB-CLOUD-0018
title: Cloud Data Platform Case Study
type: case-study
primary_domain: cloud-data-platforms
secondary_domains: [architecture, governance]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [aws-data-platform, google-bigquery, snowflake]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-CLOUD-0017]
related: [DBKB-CLOUD-0011, DBKB-CLOUD-0008]
aliases: [cloud platform scenario]
search_keywords: [cloud data case study, migration, FinOps, SLO, governance]
risk: production-critical
version_sensitive: true
review_cycle: 12m
research_packages: [RP-CLOUD-0001]
source_ids: [SRC-000098, SRC-000099, SRC-000100]
acceptance_criteria: [A bounded scenario requires architecture, migration, security, cost and reliability decisions]
---
# Cloud Data Platform Case Study

Egy regulated retailer on-prem warehouse és object-store workloadját cloud platformra migrálja, három domain consumerrel és szigorú residency/RPO követelménnyel.

Elemzendő döntések: target storage/compute, region/network, IAM/masking, data product/share boundary, batch/stream migration, query cost guard, freshness/correctness SLO, backup/restore, provider outage és exit path.

Az elemzés ne találjon ki benchmarkot vagy production eredményt. Minden feltételezés legyen jelölve, minden technikai claim linked official source-szal és minden execution result tényleges teszt outputtal alátámasztva.

## Források
- [AWS Analytics Documentation](https://docs.aws.amazon.com/analytics/)
- [Google Cloud BigQuery Documentation](https://cloud.google.com/bigquery/docs)
- [Snowflake Documentation](https://docs.snowflake.com/)
