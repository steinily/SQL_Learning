---
schema_version: 1
id: DBKB-MDM-0011
title: Master Data Quality
type: technology
primary_domain: master-data
secondary_domains: [data-quality, governance]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [openmetadata]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-MDM-0010]
related: [DBKB-DQ-0001]
aliases: [MDM quality controls]
search_keywords: [master data quality, duplicate, completeness, validity, reconciliation]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-MDM-0001]
source_ids: [SRC-000084, SRC-000085]
acceptance_criteria: [Quality dimensions, thresholds, monitoring and remediation are explained]
---
# Master Data Quality

Master data quality mérhető dimensions: completeness, validity, consistency, uniqueness, timeliness és accuracy. A domain owner definiálja a thresholdot és a critical attribute-okat; a score önmagában nem bizonyítja az üzleti helyességet.

Profiling, duplicate detection, referential checks és source-to-golden reconciliation fusson rendszeresen. A breach-hez severity, owner, due date, quarantine vagy correction workflow és trend metric tartozzon.

## Források
- [ISO 8000 Data Quality](https://www.iso.org/standard/50798.html)
- [OpenMetadata Documentation](https://docs.open-metadata.org/)
