---
schema_version: 1
id: DBKB-CLOUD-0003
title: Cloud Data Lakes
type: technology
primary_domain: cloud-data-platforms
secondary_domains: [storage, governance]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [aws-data-platform, google-bigquery]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-CLOUD-0002]
related: [DBKB-DARCH-0008]
aliases: [cloud lake]
search_keywords: [data lake, object storage, catalog, partition, lifecycle]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-CLOUD-0001]
source_ids: [SRC-000098, SRC-000099]
acceptance_criteria: [Object storage, catalog, partitioning, lifecycle, access and quality controls are covered]
---
# Cloud Data Lakes

Cloud data lake-ben a durable object storage mellé catalog, schema/format, partitioning, lifecycle, quality, lineage és access control kell. Raw landing és curated serving boundary legyen explicit, külön freshness/retention/security policy-val.

Small files, skew, unbounded partition és orphan metadata költséget és latency-t okoz. Compaction/optimization, validation, quarantine, encryption, versioning és cross-region recovery legyen automationnel és runbookkal lefedve.

## Források
- [AWS Analytics Documentation](https://docs.aws.amazon.com/analytics/)
- [Google Cloud BigQuery Documentation](https://cloud.google.com/bigquery/docs)
