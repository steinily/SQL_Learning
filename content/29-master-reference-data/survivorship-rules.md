---
schema_version: 1
id: DBKB-MDM-0007
title: Survivorship Rules
type: playbook
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
prerequisites: [DBKB-MDM-0006]
related: [DBKB-MDM-0005, DBKB-MDM-0008]
aliases: [source precedence, golden record rule]
search_keywords: [survivorship, precedence, conflict resolution, golden record]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-MDM-0001]
source_ids: [SRC-000084, SRC-000085]
acceptance_criteria: [A repeatable survivorship decision process with audit evidence is defined]
---
# Survivorship Rules

Survivorship rule dönti el, hogy ütköző source attributes esetén melyik érték kerül a golden recordba. A szabály legyen attribute-szintű, deklarálja a source precedence-t, freshness és confidence feltételeket, valamint az exception path-et.

Változás előtt mentsd a bemeneteket, a kiválasztott értéket és a döntés indokát. Ne kezeld automatikus survivorshipként a jogi identity vagy consent döntéseit; ezekhez domain owner és auditált jóváhagyás szükséges. Regression minták védjék a korábbi döntéseket.

## Források
- [ISO 8000 Data Quality](https://www.iso.org/standard/50798.html)
- [OpenMetadata Documentation](https://docs.open-metadata.org/)
