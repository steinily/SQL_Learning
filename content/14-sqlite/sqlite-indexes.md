---
schema_version: 1
id: DBKB-SQ-0010
title: SQLite Indexes
type: technology
primary_domain: sqlite
secondary_domains: [performance]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [sqlite]
sql_dialects: [sqlite]
scope: vendor-specific
prerequisites: [DBKB-SQ-0005]
related: [DBKB-SQ-0011]
aliases: [SQLite CREATE INDEX]
search_keywords: [SQLite index, CREATE INDEX, indexed lookup]
risk: caution
version_sensitive: true
review_cycle: 6m
research_packages: [RP-SQ-0001]
source_ids: [SRC-000048]
acceptance_criteria: [Index creation and trade-offs are scoped to SQLite]
---
# SQLite Indexes

SQLite indexes provide alternate access paths for table data, but every index adds storage and write-maintenance cost. Index design must be evaluated with the SQLite query planner and representative data rather than assumed from another SQL engine.

## Források
- [SQLite — The CREATE INDEX command](https://www.sqlite.org/lang_createindex.html)
