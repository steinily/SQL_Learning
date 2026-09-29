---
schema_version: 1
id: DBKB-CLOUD-0006
title: Cloud IAM and Security
type: technology
primary_domain: cloud-data-platforms
secondary_domains: [security, governance]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [aws-data-platform, google-bigquery, snowflake]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-CLOUD-0005]
related: [DBKB-SEC-0001]
aliases: [cloud data IAM]
search_keywords: [cloud IAM, least privilege, service identity, KMS, row access]
risk: security-sensitive
version_sensitive: true
review_cycle: 6m
research_packages: [RP-CLOUD-0001]
source_ids: [SRC-000098, SRC-000099, SRC-000100]
acceptance_criteria: [Identity, least privilege, encryption, key management and audit controls are covered]
---
# Cloud IAM and Security

Cloud data IAM-nál különítsd el human, workload/service és break-glass identity-t. Least privilege legyen resource-, dataset-, table-, row/column- és operation-szinten explicit, rövid élettartamú credentiallel és rotationnel.

Encryption in transit/at rest, KMS key owner/rotation, private endpoint, network policy, audit log és access review legyen baseline. Cross-account/share grant esetén a trust boundary, revocation és exfiltration control kötelező.

## Források
- [AWS Analytics Documentation](https://docs.aws.amazon.com/analytics/)
- [Google Cloud BigQuery Documentation](https://cloud.google.com/bigquery/docs)
- [Snowflake Documentation](https://docs.snowflake.com/)
