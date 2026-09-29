---
schema_version: 1
id: DBKB-CLOUD-0017
title: Multi-Cloud Data Architecture
type: technology
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
prerequisites: [DBKB-CLOUD-0016]
related: [DBKB-DARCH-0007]
aliases: [multi-cloud data]
search_keywords: [multi cloud, portability, interoperability, egress, data residency]
risk: production-critical
version_sensitive: true
review_cycle: 12m
research_packages: [RP-CLOUD-0001]
source_ids: [SRC-000098, SRC-000099, SRC-000100]
acceptance_criteria: [Multi-cloud rationale, portability, interoperability, security, cost and operations are covered]
---
# Multi-Cloud Data Architecture

Multi-cloud csak explicit driverrel (residency, resilience, acquisition, capability vagy negotiation) indokolt; a duplicate platform complexity, egress és consistency costját számszerűsítsd. Define-olj canonical contractot és portable data formatot, de a provider-specific optimization boundary-t is.

Identity, catalog, lineage, policy, key management, observability és incident response cross-cloud legyen összehangolt. Failover csak akkor claimelhető, ha tényleges replication, restore, network, IAM és reconciliation drill bizonyítja.

## Források
- [AWS Analytics Documentation](https://docs.aws.amazon.com/analytics/)
- [Google Cloud BigQuery Documentation](https://cloud.google.com/bigquery/docs)
- [Snowflake Documentation](https://docs.snowflake.com/)
