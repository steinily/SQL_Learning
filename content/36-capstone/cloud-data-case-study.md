---
schema_version: 1
id: DBKB-CAP-0020
title: Cloud Data Case Study
type: case-study
primary_domain: capstone
secondary_domains: [cloud-data-platforms, governance]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [aws-data-platform, google-bigquery, snowflake]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-CAP-0019]
related: [DBKB-CLOUD-0001]
aliases: [cloud case]
search_keywords: [cloud data, IAM, FinOps, migration, region, restore]
risk: production-critical
version_sensitive: true
review_cycle: 12m
research_packages: [RP-CAPSTONE-0001]
source_ids: [SRC-000098, SRC-000099, SRC-000100]
acceptance_criteria: [Scenario requires cloud target, IAM, cost, migration, SLO and exit decisions]
---
# Cloud Data Case Study

Regulated analytics workload cloud migrationját tervezd AWS, BigQuery vagy Snowflake célplatformra. Dönts storage/compute, region, network, IAM, masking, cost guard, observability, RPO/RTO és provider exit kérdéseiben.

Elvárt evidence: ADR, control matrix, cost assumptions, migration/reconciliation, restore test plan és incident runbook. Provider feature/pricing claimhez exact official source és retrieval date kell.

## Források
- [AWS Analytics Documentation](https://docs.aws.amazon.com/analytics/)
- [Google Cloud BigQuery Documentation](https://cloud.google.com/bigquery/docs)
- [Snowflake Documentation](https://docs.snowflake.com/)
