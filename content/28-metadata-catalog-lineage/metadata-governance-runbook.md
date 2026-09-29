---
schema_version: 1
id: DBKB-META-0014
title: Metadata Governance Runbook
type: playbook
primary_domain: metadata
secondary_domains: [governance]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [datahub, openlineage]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-META-0013]
related: []
aliases: [catalog governance runbook]
search_keywords: [catalog runbook, owner review, lineage coverage, metadata incident]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-META-0001]
source_ids: [SRC-000080, SRC-000082]
acceptance_criteria: [Onboarding, quality review, security, incident and deprecation steps are defined]
---
# Metadata Governance Runbook

Runbook kezelje source onboardingot, owner/steward assignmentot, glossary/tag reviewt, lineage quality checket, security classificationt, stale/failed ingestiont, incident escalationt és deprecationt. Minden mutationhez requester, approval, evidence, timestamp és rollback/repair path legyen.

## Források
- [DataHub Documentation](https://docs.datahub.com/)
- [OpenLineage Documentation](https://openlineage.io/docs/)
