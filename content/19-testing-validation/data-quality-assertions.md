---
schema_version: 1
id: DBKB-TEST-0010
title: Data Quality Assertions
type: technology
primary_domain: testing-validation
secondary_domains: [data-quality]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-TEST-0009]
related: []
aliases: [data quality tests]
search_keywords: [data quality, uniqueness, completeness, validity, reconciliation]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-TEST-0001]
source_ids: [SRC-000057]
acceptance_criteria: [Quality dimensions, thresholds and failure handling are described]
---
# Data Quality Assertions

Data quality assertions mérjék a completeness, uniqueness, validity, consistency, timeliness és reconciliation dimenziókat. Threshold, severity, quarantine, ownership és backfill policy legyen előre definiálva; egy aggregate count PASS nem bizonyít row-level correctness-et.

## Források
- [NIST SP 800-115](https://csrc.nist.gov/publications/detail/sp/800-115/final)
