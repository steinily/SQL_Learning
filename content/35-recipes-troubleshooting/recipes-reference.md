---
schema_version: 1
id: DBKB-REC-0060
title: Recipes Reference
type: reference
primary_domain: recipes
secondary_domains: [governance, operations]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql, sqlite, apache-kafka, openmetadata]
sql_dialects: [postgresql, tsql, mysql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-REC-0059]
related: [DBKB-REC-0058]
aliases: [recipe catalog checklist]
search_keywords: [recipe reference, troubleshooting, anti-pattern, evidence, rollback]
risk: production-critical
version_sensitive: true
review_cycle: 12m
research_packages: [RP-RECIPES-0001]
source_ids: [SRC-000001, SRC-000080, SRC-000098]
acceptance_criteria: [Recipe selection, safety and evidence reference is concise and complete]
---
# Recipes Reference

Recipe választás: domain/dialect/vendor; risk; prerequisites; read-only precheck; owner/approval; backup/recovery; expected output; validation; rollback; observability; evidence. Troubleshootinghoz symptom → evidence → containment → remediation → post-check láncot használj.

Anti-pattern reviewnél keresd a hidden assumptiont, unbounded scope-ot, owner nélküli exceptiont, execution evidence hiányát és vendor claimet linked official source nélkül. A teljes M35 manifest 60 recipe/troubleshooting/anti-pattern/runbook/reference dokumentumot tartalmaz.

## Források
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [OpenLineage Documentation](https://openlineage.io/docs/)
- [AWS Analytics Documentation](https://docs.aws.amazon.com/analytics/)
