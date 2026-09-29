---
schema_version: 1
id: DBKB-CONTRACT-0005
title: CloudEvents Contracts
type: technology
primary_domain: data-contracts
secondary_domains: [streaming, integration]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [cloudevents]
sql_dialects: []
scope: vendor-specific
prerequisites: [DBKB-CONTRACT-0004]
related: [DBKB-STREAM-0004]
aliases: [event envelope]
search_keywords: [CloudEvents, event id, source, type, subject, time, data content type]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-CONTRACT-0001]
source_ids: [SRC-000097]
acceptance_criteria: [Event context attributes, data payload, uniqueness and traceability are covered]
---
# CloudEvents Contracts

CloudEvents envelope-ben az event `id`, `source`, `specversion`, `type` és `time` contextje segíti a routingot, deduplicationt és traceability-t; a `subject`, `datacontenttype` és extension attributes domain-specifikus jelentést adhatnak.

Event contract rögzítse a uniqueness/idempotency policy-t, payload schema/versiont, orderingt, retry/replayt és PII classificationt. A protocol binding conversionnél ellenőrizd, hogy az envelope attributes és data sértetlenül megmaradnak-e.

## Forrás
- [CloudEvents](https://cloudevents.io/)
