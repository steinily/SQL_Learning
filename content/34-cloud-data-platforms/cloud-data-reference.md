---
schema_version: 1
id: DBKB-CLOUD-0015
title: Cloud Data Reference
type: reference
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
prerequisites: [DBKB-CLOUD-0014]
related: [DBKB-DARCH-0006]
aliases: [cloud data checklist]
search_keywords: [cloud data checklist, IAM, cost, SLO, region, restore]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-CLOUD-0001]
source_ids: [SRC-000098, SRC-000099, SRC-000100]
acceptance_criteria: [Cloud data platform selection and go-live checklist is provided]
---
# Cloud Data Reference

Checklist: workload/data classification; region/residency; storage/compute; partition/query; IAM/network/encryption; catalog/lineage; quality/freshness; quota/SLO; backup/restore/RPO/RTO; cost/egress; sharing/revocation; observability; migration/rollback; provider exit.

Go-live előtt validate account/project boundaries, policy tests, representative query, restore evidence, budget alert, incident owner, contract compatibility és decommission plan.

## Források
- [AWS Analytics Documentation](https://docs.aws.amazon.com/analytics/)
- [Google Cloud BigQuery Documentation](https://cloud.google.com/bigquery/docs)
- [Snowflake Documentation](https://docs.snowflake.com/)
