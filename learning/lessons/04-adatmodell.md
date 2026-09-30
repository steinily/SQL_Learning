# 8. Adatmodell és megszorítások

Az adatmodell nem pusztán táblanevek listája: a kulcsok és a megszorítások (`constraints`) üzleti szabályokat védenek. A `NOT NULL`, `UNIQUE`, `CHECK`, `PRIMARY KEY` és `FOREIGN KEY` hibás állapotok létrejöttét akadályozza.

## Tanulási eredmény

A lecke végére meg tudod indokolni, melyik adat melyik táblába kerüljön, és legalább három hibás állapotot megszorítással tudsz megelőzni.

Nézd meg a [schema.sql](../sql/schema.sql) fájlt, és keresd meg benne mind az öt típust. Ezután olvasd el a [Constraints](../../content/01-foundations/constraints.md) és [Normalization](../../content/05-data-modeling/normalization.md) cikkeket.

## Feladat

Írd le saját szavaiddal, mi romolna el, ha az `order_items` helyett egyetlen `product_id` oszlopot tennénk az `orders` táblába.

Ezután oldd meg a [`04-constraints.sql`](../exercises/04-constraints.sql) feladatot, és ellenőrizd a [mintamegoldást](../solutions/04-constraints.sql).

Megjegyzés: ebben a feladatban szándékosan kapsz constraint hibákat; a hiba megértése a cél, nem a hibás beszúrás sikeres végrehajtása.
