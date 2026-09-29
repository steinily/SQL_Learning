---
schema_version: 1
id: DBKB-MDM-0010
title: Master Data Integration
type: technology
primary_domain: master-data
secondary_domains: [data-integration, governance]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [openmetadata]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-MDM-0008]
related: [DBKB-MDM-0005, DBKB-MDM-0007]
aliases: [MDM integration, master data distribution]
search_keywords: [master data integration, publish subscribe, CDC, reconciliation]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-MDM-0001]
source_ids: [SRC-000084, SRC-000085]
acceptance_criteria: [Inbound matching, canonicalization, outbound distribution and reconciliation are covered]
---
# Master Data Integration

Az integration négy kontrollpontja: inbound profiling és identity matching; canonicalization és survivorship; outbound distribution; reconciliation és exception handling. A transport lehet batch, API, event vagy CDC, de minden útvonalon legyen idempotency key, schema contract és replay stratégia.

A golden record publikálása ne legyen automatikus bizonyíték a downstream helyességére. Mérd a késést, duplicate-ot, rejected rekordokat és source-to-target reconciliation eltérést; a hibákat quarantine queue-ba és steward queue-ba irányítsd.

## Források
- [ISO 8000 Data Quality](https://www.iso.org/standard/50798.html)
- [OpenMetadata Documentation](https://docs.open-metadata.org/)
