# Feladatok futtatása

## Munkafolyamat

1. Másold ki az adott feladatot `my-answer.sql` néven.
2. A kommentek alatt írd meg a saját SQL-edet.
3. Futtasd a laboradaton:

```bash
python3 scripts/learning_runner.py --file my-answer.sql
```

4. Ellenőrizd a sorokat, a sorrendet, a NULL-kezelést és a duplikációkat.
5. Csak utána nyisd meg a `learning/solutions/` megfelelő fájlját.

A futtató minden alkalommal új adatbázist hoz létre, ezért a módosítási feladatok nem változtatják meg a repó adatait.

## Feladattérkép

| Téma | Feladat |
|---|---|
| SELECT | `01-select.sql` |
| JOIN és aggregáció | `02-join.sql` |
| CTE, ablakfüggvény, CASE | `03-advanced.sql`, `09-case.sql` |
| Megszorítások | `04-constraints.sql` |
| Tranzakció | `05-transactions.sql` |
| NULL | `06-null.sql` |
| HAVING | `07-having.sql` |
| Al-lekérdezések | `08-subqueries.sql` |
| Index és terv | `10-index.sql` |
| Záróprojekt | `11-project.md` |
| Window function | `12-window.sql` |
| Top-N csoportonként | `13-top-n.sql` |
| Rekurzív CTE | `14-recursive.sql` |
| Query optimalizálás | `15-optimization.sql` |
| Indexstratégia | `16-index-strategy.sql` |
| Locking és konkurencia | `17-locking.sql` |
| Haladó projekt | `18-advanced-project.md` |

## Mit jelent a jó válasz?

Nem elég, hogy a lekérdezés lefut. A jó megoldás a kérdésnek megfelelő sorokat adja vissza, egyértelmű oszlopneveket használ, kezeli a lehetséges NULL/duplikáció eseteket, és ahol számít, determinisztikus sorrendet ad.
