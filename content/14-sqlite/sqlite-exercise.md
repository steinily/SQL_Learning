---
schema_version: 1
id: DBKB-SQ-0014
title: SQLite Exercise
type: exercise
primary_domain: sqlite
secondary_domains: [validation]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [sqlite]
sql_dialects: [sqlite]
scope: vendor-specific
prerequisites: [DBKB-SQ-0009, DBKB-SQ-0011, DBKB-SQ-0012]
related: [DBKB-SQ-0013]
aliases: [SQLite validation exercise]
search_keywords: [SQLite exercise, foreign key check, query plan, restore test]
risk: caution
version_sensitive: true
review_cycle: 6m
research_packages: [RP-SQ-0001]
source_ids: [SRC-000048]
acceptance_criteria: [Exercise defines evidence to collect without claiming unexecuted results]
---
# SQLite Exercise

Készíts SQLite validation plan-t: dokumentáld a runtime version-t és compile options-t, ellenőrizd a foreign key enforcement state-et, rögzíts egy target buildből származó query plan-t, majd készíts backupot és restore verification-t. A feladat eredménye csak tényleges futtatás után jelölhető execution-verified állapotúként.

## Források
- [SQLite — Documentation](https://www.sqlite.org/docs.html)
