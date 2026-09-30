# SQL Learning Path

Ez a javasolt sorrend annak, aki nulláról szeretne használható SQL-tudást szerezni. Egy szakasz akkor kész, ha a tanuló a feladatokat segítség nélkül megoldja és el tudja mondani, miért azt a lekérdezést választotta.

| Szakasz | Mit tanulsz? | Lecke | Referencia |
|---|---|---|---|
| 0. Környezet | adatbázis, tábla, sor, oszlop, séma | [00-környezet](learning/lessons/00-kornyezet.md) | [Database Fundamentals](content/01-foundations/database-fundamentals.md) |
| 1. Lekérdezés | `SELECT`, `FROM`, `WHERE`, `ORDER BY`, `LIMIT` | [01-lekérdezés](learning/lessons/01-lekerdezes.md) | [SELECT Fundamentals](content/02-sql-fundamentals/select-fundamentals.md) |
| 2. Kapcsolás | kulcsok, `JOIN`, aggregáció, `GROUP BY` | [02-kapcsolás](learning/lessons/02-kapcsolas-es-aggregacio.md) | [Join Fundamentals](content/02-sql-fundamentals/join-fundamentals.md) |
| 3. Összetett lekérdezés | `CASE`, CTE, al-lekérdezés, ablakfüggvény | [03-összetett](learning/lessons/03-osszetett-lekerdezesek.md) | [CTE Fundamentals](content/03-intermediate-sql/cte-fundamentals.md) |
| 4. Adatmodell | elsődleges/külső kulcs, megszorítások, normalizálás | [04-adatmodell](learning/lessons/04-adatmodell.md) | [Data Modeling Overview](content/05-data-modeling/data-modeling-overview.md) |
| 5. Biztonságos módosítás | `INSERT`, `UPDATE`, `DELETE`, tranzakció | [05-módosítás](learning/lessons/05-adatmodositas-es-tranzakcio.md) | [Transactions](content/07-transactions-and-concurrency/transactions-and-concurrency-overview.md) |
| 6. Következő szint | index, execution plan, dialektusok, projekt | [06-tovább](learning/lessons/06-tovabb.md) | [Indexing](content/08-indexing/indexing-overview.md) |

Az első öt szakasz után a tanuló képes legyen egy kis üzleti kérdést táblákra és lekérdezésre bontani. Ezután a `content/` megfelelő moduljaiban érdemes mélyíteni, nem mind a 919 cikket sorrendben elolvasni.

## Oktatónak

Egy 90 perces alkalomhoz válassz egy leckét: 15 perc magyarázat, 20 perc közös kódolás, 35 perc feladat, 10 perc megbeszélés, 10 perc ellenőrző kérdés. A megoldások külön könyvtárban vannak.
