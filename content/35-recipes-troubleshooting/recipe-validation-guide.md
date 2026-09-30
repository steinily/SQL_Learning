---
schema_version: 1
id: DBKB-REC-0058
title: Recipe Validation Guide
type: reference
primary_domain: recipes
secondary_domains: [testing, governance]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, apache-kafka, openmetadata]
sql_dialects: [postgresql]
scope: cross-vendor
prerequisites: [DBKB-REC-0057]
related: [DBKB-TEST-0001]
aliases: [recipe QA checklist]
search_keywords: [recipe validation, precheck, execution evidence, rollback, audit]
risk: production-critical
version_sensitive: false
review_cycle: 12m
research_packages: [RP-RECIPES-0001]
source_ids: [SRC-000001, SRC-000080]
acceptance_criteria: [Recipe QA includes metadata, source, safety, execution and post-check requirements]
---
# Recipe Validation Guide

Recipe QA checklist: valid metadata/dialect/scope; authoritative source; prerequisites; read-only precheck; parameterization; destructive risk/approval; expected output; rollback/abort; observability; data/security impact; actual execution output; post-check; evidence retention.

`execution-verified` csak futtatott command, environment/version, timestamp, output és reviewer evidence után használható. Unsupported dialect vagy unavailable service esetén markolj uncertainty-t, ne hamisíts PASS-t.

## Források
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [OpenLineage Documentation](https://openlineage.io/docs/)
