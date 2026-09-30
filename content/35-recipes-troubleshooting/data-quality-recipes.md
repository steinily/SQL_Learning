---
schema_version: 1
id: DBKB-REC-0015
title: Data Quality Recipes
type: playbook
primary_domain: recipes
secondary_domains: [data-quality, governance]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql, sqlite]
sql_dialects: [postgresql, tsql, mysql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-REC-0014]
related: [DBKB-DQ-0001]
aliases: [quality rule recipe]
search_keywords: [data quality, completeness, uniqueness, validity, reconciliation]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-RECIPES-0001]
source_ids: [SRC-000001, SRC-000098]
acceptance_criteria: [Quality checks, thresholds, quarantine, remediation and evidence are actionable]
---
# Data Quality Recipes

Quality recipe tartalmazzon dimensiont, rule-t, scope-ot, thresholdot, severityt, ownert és evaluation window-t. Ellenőrizd completeness, validity, uniqueness, referential integrity, timeliness és reconciliation értéket; sample score nem bizonyítja a teljes dataset correctnessét.

Breach esetén quarantine vagy reject path, incident owner, due date, correction/replay és post-fix recheck kell. Tartsd meg input snapshot, rule version, result count és execution timestamp evidence-ét; threshold change legyen governance döntés.

## Források
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [AWS Analytics Documentation](https://docs.aws.amazon.com/analytics/)
