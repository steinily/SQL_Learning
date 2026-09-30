# SQL Learning Path

Ez a javasolt sorrend annak, aki nulláról szeretne használható SQL-tudást szerezni. Egy szakasz akkor kész, ha a tanuló a feladatokat segítség nélkül megoldja és el tudja mondani, miért azt a lekérdezést választotta.

| Szakasz | Mit tanulsz? | Lecke | Referencia |
|---|---|---|---|
| 0. Környezet | adatbázis, tábla, sor, oszlop, séma | [00-környezet](learning/lessons/00-kornyezet.md) | [Database Fundamentals](content/01-foundations/database-fundamentals.md) |
| 1. Lekérdezés | `SELECT`, `FROM`, `WHERE`, `ORDER BY`, `LIMIT` | [01-lekérdezés](learning/lessons/01-lekerdezes.md) | [SELECT Fundamentals](content/02-sql-fundamentals/select-fundamentals.md) |
| 2. Kapcsolás | kulcsok, `JOIN`, aggregáció, `GROUP BY` | [02-kapcsolás](learning/lessons/02-kapcsolas-es-aggregacio.md) | [Join Fundamentals](content/02-sql-fundamentals/join-fundamentals.md) |
| 3. Összetett lekérdezés | CTE, ablakfüggvény | [03-összetett](learning/lessons/03-osszetett-lekerdezesek.md) | [CTE Fundamentals](content/03-intermediate-sql/cte-fundamentals.md) |
| 4. NULL-kezelés | `NULL`, `COALESCE`, `NULLIF` | [04-NULL](learning/lessons/04-null-es-coalesce.md) | [NULL Fundamentals](content/01-foundations/null-fundamentals.md) |
| 5. Csoportok szűrése | `GROUP BY`, `HAVING` | [05-HAVING](learning/lessons/05-having.md) | [HAVING](content/02-sql-fundamentals/having.md) |
| 6. Al-lekérdezések | scalar subquery, `EXISTS`, `IN` | [06-al-lekérdezések](learning/lessons/06-al-lekerdezesek.md) | [Subquery Fundamentals](content/03-intermediate-sql/subquery-fundamentals.md) |
| 7. Feltételes logika | `CASE` | [07-CASE](learning/lessons/07-case.md) | [CASE Expressions](content/03-intermediate-sql/case-expressions.md) |
| 8. Adatmodell | elsődleges/külső kulcs, megszorítások, normalizálás | [08-adatmodell](learning/lessons/04-adatmodell.md) | [Data Modeling Overview](content/05-data-modeling/data-modeling-overview.md) |
| 9. Biztonságos módosítás | `INSERT`, `UPDATE`, `DELETE`, tranzakció | [09-módosítás](learning/lessons/05-adatmodositas-es-tranzakcio.md) | [Transactions](content/07-transactions-and-concurrency/transactions-and-concurrency-overview.md) |
| 10. Index és terv | index, `EXPLAIN QUERY PLAN` | [10-index](learning/lessons/10-index-es-explain.md) | [Indexing Overview](content/08-indexing/indexing-overview.md) |
| 11. Következő szint | dialektusok és projekt | [11-tovább](learning/lessons/06-tovabb.md) | [Query Performance](content/09-query-performance-and-optimization/query-performance-overview.md) |

Az első tíz szakasz után a tanuló képes legyen egy kis üzleti kérdést táblákra és lekérdezésre bontani, az eredményt ellenőrizni és a biztonsági/teljesítménybeli következményeket felismerni. Ezután a `content/` megfelelő moduljaiban érdemes mélyíteni, nem mind a 919 cikket sorrendben elolvasni.

## Oktatónak

Egy 90 perces alkalomhoz válassz egy leckét: 15 perc magyarázat, 20 perc közös kódolás, 35 perc feladat, 10 perc megbeszélés, 10 perc ellenőrző kérdés. A megoldások külön könyvtárban vannak.
