# 5. Adatmódosítás és tranzakció

Az `INSERT`, `UPDATE` és `DELETE` módosítja az adatot. Módosítás előtt ugyanazzal a feltétellel futtass ellenőrző `SELECT`-et, majd használd a `BEGIN` / `COMMIT` / `ROLLBACK` tranzakciós határokat.

## Tanulási eredmény

Biztonságosan meg tudsz tervezni egy módosítást: előzetes darabszám-ellenőrzéssel, tranzakcióval és visszagörgetési tervvel.

```sql
BEGIN;
UPDATE products SET unit_price = unit_price * 1.10 WHERE category = 'book';
-- ellenőrzés: SELECT ...
ROLLBACK;
```

A labor adatbázisa memóriabeli, ezért ez csak tanulási példa. Éles adatbázisban a jogosultság, mentés, naplózás és concurrency is része a biztonságos módosításnak.

Gyakorlat: [`05-transactions.sql`](../exercises/05-transactions.sql), majd [mintamegoldás](../solutions/05-transactions.sql).
