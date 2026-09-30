---
schema_version: 1
id: DBKB-REC-0059
title: Troubleshooting Exercise
type: exercise
primary_domain: recipes
secondary_domains: [operations, reliability]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, apache-kafka, openmetadata]
sql_dialects: [postgresql]
scope: cross-vendor
prerequisites: [DBKB-REC-0058]
related: [DBKB-REC-0039, DBKB-REC-0057]
aliases: [incident lab]
search_keywords: [troubleshooting exercise, slow query, pipeline lag, schema drift, recovery]
risk: production-critical
version_sensitive: false
review_cycle: 12m
research_packages: [RP-RECIPES-0001]
source_ids: [SRC-000001, SRC-000080]
acceptance_criteria: [Learner produces evidence-based diagnosis, containment, recovery and post-incident artifacts]
---
# Troubleshooting Exercise

Scenario: egy schema change után slow query, pipeline lag és quality breach jelenik meg; a consumer contract is failing.

Készíts timeline-t, hypothesis/evidence táblát, blast-radius mapet, containment és rollback döntést, recovery validationt, communicationt és post-incident action listát. Külön jelöld az observed, inferred és executed állításokat.

Elvárt eredmény: query/lock/pipeline evidence, contract diff, recovery decision tree, owner/SLO matrix és reprodukálható test plan. Fiktív execution outputot vagy benchmarkot ne adj meg.

## Források
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [OpenLineage Documentation](https://openlineage.io/docs/)
