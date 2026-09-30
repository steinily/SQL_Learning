---
schema_version: 1
id: DBKB-REC-0057
title: Recovery Decision Tree
type: reference
primary_domain: recipes
secondary_domains: [disaster-recovery, operations]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, apache-kafka, openmetadata]
sql_dialects: [postgresql]
scope: cross-vendor
prerequisites: [DBKB-REC-0056]
related: [DBKB-DR-0001]
aliases: [recovery tree]
search_keywords: [recovery decision, rollback, restore, replay, failover, quarantine]
risk: production-critical
version_sensitive: false
review_cycle: 12m
research_packages: [RP-RECIPES-0001]
source_ids: [SRC-000001, SRC-000080]
acceptance_criteria: [Recovery choices are based on evidence, RPO/RTO, reversibility and correctness]
---
# Recovery Decision Tree

1. Is the source of truth known and intact? If no, preserve evidence and escalate; do not overwrite.
2. Is the change reversible within the SLO? If yes, abort/rollback and verify; if no, choose forward-fix or restore boundary.
3. Is replay idempotent and checkpoint known? If yes, bounded replay; if no, quarantine and manual reconciliation.
4. Is security or residency impact present? Fence access and involve security/privacy owner.

Every branch records RPO/RTO, owner, approval, evidence, validation and residual uncertainty. Recovery completion requires business invariant, quality, lineage, consumer and audit checks.

## Források
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [OpenLineage Documentation](https://openlineage.io/docs/)
