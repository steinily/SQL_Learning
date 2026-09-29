---
schema_version: 1
id: DBKB-META-0011
title: Catalog Security
type: technology
primary_domain: metadata
secondary_domains: [security-privacy]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [datahub, openlineage]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-META-0010]
related: []
aliases: [metadata access control]
search_keywords: [catalog security, metadata ACL, sensitive tags, lineage access]
risk: security-sensitive
version_sensitive: true
review_cycle: 6m
research_packages: [RP-META-0001]
source_ids: [SRC-000080, SRC-000082]
acceptance_criteria: [Catalog identity, access, sensitive metadata and audit controls are covered]
---
# Catalog Security

Catalog metadata is sensitive lehet: schema, PII tags, owners, lineage és access context information disclosure-t okozhat. Enforce-olj catalog identity/role, entity/field scope, ingestion credential, API audit, redaction és retention policy-t; lineage visibility ne bypassolja source data authorizationt.

## Források
- [DataHub Documentation](https://docs.datahub.com/)
- [OpenLineage Documentation](https://openlineage.io/docs/)
