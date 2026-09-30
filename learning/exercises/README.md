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

## Mit jelent a jó válasz?

Nem elég, hogy a lekérdezés lefut. A jó megoldás a kérdésnek megfelelő sorokat adja vissza, egyértelmű oszlopneveket használ, kezeli a lehetséges NULL/duplikáció eseteket, és ahol számít, determinisztikus sorrendet ad.
