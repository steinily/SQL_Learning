---
schema_version: 1
id: DBKB-CAP-0037
title: Security Exercise
type: exercise
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
prerequisites: [DBKB-CAP-0036]
related: [DBKB-SEC-0001]
aliases: [security lab]
search_keywords: [security exercise, IAM, TLS, masking, audit, incident]
risk: security-sensitive
version_sensitive: false
review_cycle: 12m
research_packages: [RP-CAPSTONE-0001]
source_ids: [SRC-000001, SRC-000087]
acceptance_criteria: [Learner implements least privilege, encryption, masking, audit and incident validation]
---
# Security Exercise

Tervezd meg egy service identity least-privilege accessét, TLS/key rotationt, sensitive column maskinget, auditot és break-glass pathot. Injectálj unauthorized read és credential rotation eseményt.

Elvárt evidence: positive/negative access tests, audit log, revoke/rotate output, data classification és post-incident actions. Secretet vagy valós sensitive payloadot ne használj.

## Források
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [Apache Kafka Documentation](https://kafka.apache.org/documentation/)
