---
schema_version: 1
id: DBKB-REC-0035
title: Data Quality Troubleshooting
type: troubleshooting
primary_domain: recipes
secondary_domains: [data-quality, governance]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql, sqlite]
sql_dialects: [postgresql, tsql, mysql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-REC-0034]
related: [DBKB-DQ-0001]
aliases: [quality incident runbook]
search_keywords: [quality breach, duplicate, "null", freshness, reconciliation]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-RECIPES-0001]
source_ids: [SRC-000001, SRC-000098]
acceptance_criteria: [Rule, scope, upstream evidence, quarantine, remediation and recheck are covered]
---
# Data Quality Troubleshooting

Capture rule/version, scope/window, failed count, sample evidence, upstream batch/run, schema and freshness watermark. Distinguish source defect, transformation defect, late data, duplicate replay, reference mismatch és rule regression.

Containment lehet quarantine, consumer warning, last-known-good publish vagy controlled replay. Remediation után re-run the same rule, compare trend, reconcile downstream és record owner/due date; threshold módosítás ne legyen silent fix.

## Források
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [AWS Analytics Documentation](https://docs.aws.amazon.com/analytics/)
