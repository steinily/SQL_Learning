---
schema_version: 1
id: DBKB-ISQL-0024
title: Views
type: concept
primary_domain: intermediate-sql
secondary_domains: [data-modeling, security]
levels: [intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql, sqlite]
sql_dialects: [postgresql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-SQL-0022, DBKB-ISQL-0023]
related: [DBKB-ISQL-0025]
aliases: [virtual table, saved query]
search_keywords: [create view, abstraction, schema interface, dependency]
risk: caution
version_sensitive: true
review_cycle: 6m
research_packages: [RP-ISQL-0003]
source_ids: [SRC-000037]
acceptance_criteria:
  - Reusable named query interface-ként mutatja be a view-t.
  - Tárgyalja a dependency security és change-management kérdéseket.
  - Ephemeral környezetben futtatott view példát ad.
---
# Views

View nevet ad egy querynek, és table-szerű interface-ként hivatkozható. Elrejthet schema részleteket,
központosíthat reusable projectiont és stabil consumer contractot adhat.

```sql
CREATE VIEW active_customer AS
SELECT customer_id, customer_name
FROM customer
WHERE status = 'ACTIVE';
```

A normál view nem általánosan stored result; materialized view külön object és vendor-specific
lifecycle. View-on belüli `ORDER BY` nem helyettesíti a consumer query orderingjét.

Column rename/type change, underlying dependency és `SELECT *` contract breaket okozhat. Production
változást versioned migrationnel és dependent-object impact analysisszel végezz. Updatability,
invoker/definer security és row-filter security behavior engine-specific; view önmagában nem
automatikus security boundary.

A `SQL-ISQL-0024` ephemeral SQLite adatbázisban létrehoz egy view-t, majd exact projectiont olvas.
Ez nem bizonyít PostgreSQL view-security vagy updatability behavior-t.

## Források

- [PostgreSQL 18 Tutorial — Views](https://www.postgresql.org/docs/18/tutorial-views.html)
