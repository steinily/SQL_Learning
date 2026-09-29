---
schema_version: 1
id: DBKB-MDM-0013
title: Master Data Troubleshooting
type: troubleshooting
primary_domain: master-data
secondary_domains: [data-quality, operations]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [openmetadata]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-MDM-0012]
related: [DBKB-MDM-0010, DBKB-MDM-0011]
aliases: [MDM incident runbook]
search_keywords: [duplicate golden record, stale master data, reconciliation failure]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-MDM-0001]
source_ids: [SRC-000084, SRC-000085]
acceptance_criteria: [Symptom-to-check-to-remediation paths cover common MDM incidents]
---
# Master Data Troubleshooting

**Duplicate golden record:** freeze downstream publish, inspect matching keys and source evidence, re-run a dry-run merge, then obtain steward approval before correcting. Preserve the losing record and merge audit trail.

**Stale or missing value:** compare source timestamp, integration lag, rejected/quarantine counts and effective dates. Repair the pipeline or reference lifecycle state; do not overwrite with an unverified manual value.

**Reconciliation mismatch:** identify the last consistent checkpoint, compare counts and hashes by batch/window, replay idempotently, and open an exception with owner and impact. Record evidence and rollback decision.

## Források
- [ISO 8000 Data Quality](https://www.iso.org/standard/50798.html)
- [OpenMetadata Documentation](https://docs.open-metadata.org/)
