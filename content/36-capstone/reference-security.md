---
schema_version: 1
id: DBKB-CAP-0056
title: Reference Security
type: reference
primary_domain: capstone
secondary_domains: [security, governance]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, apache-kafka]
sql_dialects: [postgresql]
scope: cross-vendor
prerequisites: [DBKB-CAP-0055]
related: [DBKB-SEC-0001]
aliases: [security checklist]
search_keywords: [security reference, IAM, TLS, least privilege, audit, masking]
risk: security-sensitive
version_sensitive: false
review_cycle: 12m
research_packages: [RP-CAPSTONE-0001]
source_ids: [SRC-000001, SRC-000087]
acceptance_criteria: [Security design, operation and incident controls are summarized]
---
# Reference Security

Checklist: identity separation; least privilege; network boundary; TLS/mTLS; encryption/key rotation; sensitive classification/masking; audit; secret redaction; backup/share control; revoke/rotate; incident/legal handoff; negative access test.

Security baseline legyen versioned, reviewed és evidence-backed; emergency exceptionnek owner, expiry és post-fix remediation kell.

## Források
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [Apache Kafka Documentation](https://kafka.apache.org/documentation/)
