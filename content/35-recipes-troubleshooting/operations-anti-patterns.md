---
schema_version: 1
id: DBKB-REC-0053
title: Operations Anti-Patterns
type: error
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
prerequisites: [DBKB-REC-0052]
related: [DBKB-OPS-0001]
aliases: [operations mistakes]
search_keywords: [no runbook, no owner, manual drift, blind restart, missing rollback]
risk: production-critical
version_sensitive: false
review_cycle: 12m
research_packages: [RP-RECIPES-0001]
source_ids: [SRC-000001, SRC-000080]
acceptance_criteria: [Operations anti-patterns include observability, ownership and rollback remediation]
---
# Operations Anti-Patterns

Anti-pattern az owner/runbook nélküli alert, manual configuration drift, blind restart/failover, unbounded retry, backup restore drill hiánya, change window nélküli destructive action és „green” monitor business validation nélkül.

Detectáld alert-to-runbook coverage, config diff, incident repeat, restore cadence és change evidence alapján. Remediation automation, peer review, canary, rollback, SLO/error budget és post-incident action owner legyen.

## Források
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [OpenLineage Documentation](https://openlineage.io/docs/)
