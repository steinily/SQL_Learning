---
schema_version: 1
id: DBKB-ASQL-0016
title: Hierarchy Processing Patterns
type: concept
primary_domain: advanced-sql
secondary_domains: [data-modeling]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql, sqlite]
sql_dialects: [postgresql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-ISQL-0022, DBKB-ISQL-0006]
related: [DBKB-ASQL-0013]
aliases: [tree traversal, recursive hierarchy]
search_keywords: [hierarchy, recursive cte, path, depth, cycle]
risk: caution
version_sensitive: true
review_cycle: 6m
research_packages: [RP-ASQL-0002]
source_ids: [SRC-000032]
acceptance_criteria:
  - Bemutatja a root descendant depth és path outputokat.
  - Kötelező cycle és resource guardot ír elő.
  - Futtatható bounded tree traversal példát ad.
---
# Hierarchy Processing Patterns

Adjacency-list hierarchy feldolgozásához recursive CTE root anchorből indul, majd parent–child edge-en
bővül. Hasznos output a node, root, depth és traversal path.

Tree assumptiont constraint nélkül nem szabad adottnak venni: orphan, multiple parent és cycle
lehetséges. Production queryben cycle detection vagy visited-path guard, maximum depth és resource
limit szükséges. Depth limit önmagában nem bizonyít adatkorrektséget.

Traversal calculation order nem presentation order. Stabil hierarchy rendereléshez explicit sort
path kell, amelynek encodingja sibling ordert és identifier collisiont is kezeli.

A `SQL-ASQL-0016` egy háromszintű acyclic tree-t jár be explicit depth guarddal SQLite-on, és exact
node-depth outputot ellenőriz.

## Források

- [PostgreSQL 18 — WITH Queries](https://www.postgresql.org/docs/18/queries-with.html)
