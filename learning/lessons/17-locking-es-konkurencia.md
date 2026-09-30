# 17. Locking és konkurencia

## Cél

Értsd meg a blocking, timeout és deadlock közötti különbséget, és tudd, miért kell rövid tranzakció, stabil erőforrás-sorrend és retry stratégia.

- **Blocking:** egy tranzakció vár a másik által tartott lockra.
- **Timeout:** a várakozás elérte a beállított határt.
- **Deadlock:** két vagy több tranzakció körkörösen egymásra vár.

A labor demója két SQLite-kapcsolatot használ ideiglenes fájlban, és szándékosan bemutat egy rövid lock-wait helyzetet:

```bash
python3 scripts/locking_demo.py
```

Ez nem helyettesít PostgreSQL, SQL Server vagy MySQL concurrency tesztet: az isolation level, lock mode és MVCC-viselkedés vendorfüggő.

## Gyakorlat

Oldd meg a [`17-locking.sql`](../exercises/17-locking.sql) feladatot. A referencia: [Locking Fundamentals](../../content/07-transactions-and-concurrency/locking-fundamentals.md).
