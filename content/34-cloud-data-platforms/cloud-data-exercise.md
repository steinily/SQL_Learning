---
schema_version: 1
id: DBKB-CLOUD-0014
title: Cloud Data Exercise
type: exercise
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
prerequisites: [DBKB-CLOUD-0013]
related: [DBKB-CLOUD-0008, DBKB-CLOUD-0011]
aliases: [cloud data lab]
search_keywords: [cloud data exercise, FinOps, IAM, migration, reliability]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-CLOUD-0001]
source_ids: [SRC-000098, SRC-000099, SRC-000100]
acceptance_criteria: [Learner produces cloud target architecture, IAM, cost, migration and recovery evidence]
---
# Cloud Data Exercise

Tervezd meg egy regulated analytics workload cloud migrationjét AWS, BigQuery vagy Snowflake célplatformra.

1. Határozd meg storage/compute, network, IAM, classification és region döntéseket.
2. Készíts FinOps unit-economics és quota/observability tervet.
3. Definiálj dual-run, reconciliation, cutover, RPO/RTO és rollback lépéseket.
4. Mutasd be a share/revocation és incident runbookot.

Elvárt eredmény: ADR, target diagram, control matrix, cost model, migration plan és test evidence. Provider feature vagy benchmark állítás csak official docs és tényleges futtatási output alapján használható.

## Források
- [AWS Analytics Documentation](https://docs.aws.amazon.com/analytics/)
- [Google Cloud BigQuery Documentation](https://cloud.google.com/bigquery/docs)
- [Snowflake Documentation](https://docs.snowflake.com/)
