---
schema_version: 1
id: DBKB-CAP-0014
title: Security Case Study
type: case-study
primary_domain: capstone
secondary_domains: [security, governance]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, apache-kafka]
sql_dialects: [postgresql]
scope: cross-vendor
prerequisites: [DBKB-CAP-0013]
related: [DBKB-SEC-0001]
aliases: [security case]
search_keywords: [database security, least privilege, credential leak, audit, masking]
risk: security-sensitive
version_sensitive: false
review_cycle: 12m
research_packages: [RP-CAPSTONE-0001]
source_ids: [SRC-000001, SRC-000087]
acceptance_criteria: [Scenario requires identity, access, encryption, audit, containment and recovery decisions]
---
# Security Case Study

Egy service identity túlzott granttal exportál sensitive customer data-t. Határozd meg a blast radius-t, access/audit evidence-et, containment/rotationt, legal/privacy handoffot és least-privilege corrective controlt.

Elvárt evidence: principal/resource/action/time, logs, data classification, revoked path, negative access test, key rotation és post-incident actions. Fiktív breach vagy production impact nem állítható bizonyíték nélkül.

## Források
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [Apache Kafka Documentation](https://kafka.apache.org/documentation/)
