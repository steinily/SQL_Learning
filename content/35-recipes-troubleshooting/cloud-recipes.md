---
schema_version: 1
id: DBKB-REC-0026
title: Cloud Recipes
type: playbook
primary_domain: recipes
secondary_domains: [cloud-data-platforms, operations]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [aws-data-platform, google-bigquery, snowflake]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-REC-0025]
related: [DBKB-CLOUD-0001]
aliases: [cloud data runbook]
search_keywords: [cloud data, IAM, region, budget, quota, backup, rollback]
risk: production-critical
version_sensitive: true
review_cycle: 12m
research_packages: [RP-RECIPES-0001]
source_ids: [SRC-000098, SRC-000099, SRC-000100]
acceptance_criteria: [Cloud data preflight, change, validation, rollback and evidence steps are defined]
---
# Cloud Recipes

Cloud data recipe preflight: target account/project, region és residency; identity/least privilege; network path; quota; budget/alert; encryption/key ownership; dependency and rollback checkpoint. Provider feature and limit claimset mindig az adott official documentation verziójával kell ellenőrizni.

Végrehajtási minta: dry-run vagy plan; scoped change; observable migration/query/load; data count/schema/quality validation; cost and quota review; rollback or cleanup; timestamped evidence. Production execution status csak tényleges futtatás után adható.

## Források
- [AWS Analytics Documentation](https://docs.aws.amazon.com/analytics/)
- [Google Cloud BigQuery Documentation](https://cloud.google.com/bigquery/docs)
- [Snowflake Documentation](https://docs.snowflake.com/)
