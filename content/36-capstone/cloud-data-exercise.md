---
schema_version: 1
id: DBKB-CAP-0043
title: Cloud Data Exercise
type: exercise
primary_domain: capstone
secondary_domains: [cloud-data-platforms, finops]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [aws-data-platform, google-bigquery, snowflake]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-CAP-0042]
related: [DBKB-CLOUD-0001]
aliases: [cloud lab]
search_keywords: [cloud data exercise, IAM, cost, migration, RPO, restore]
risk: production-critical
version_sensitive: true
review_cycle: 12m
research_packages: [RP-CAPSTONE-0001]
source_ids: [SRC-000098, SRC-000099, SRC-000100]
acceptance_criteria: [Learner designs cloud target, controls, migration, FinOps and recovery evidence]
---
# Cloud Data Exercise

Válassz cloud targetet regulated warehouse/lake workloadhoz; definiáld region/residency, IAM/network/encryption, storage/compute, quality, observability, budget/quota és provider exit döntést.

Készíts migration dual-run, reconciliation, restore/failover és cost unit-economics tervet. Feature/pricing/benchmark csak timestamped official source és execution outputtal állítható.

## Források
- [AWS Analytics Documentation](https://docs.aws.amazon.com/analytics/)
- [Google Cloud BigQuery Documentation](https://cloud.google.com/bigquery/docs)
- [Snowflake Documentation](https://docs.snowflake.com/)
