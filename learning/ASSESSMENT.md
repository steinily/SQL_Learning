# Önálló ellenőrzés

## Szintek

- **Bronz:** a tanuló el tudja olvasni a sémát, és egyszerű `SELECT` lekérdezéseket ír.
- **Ezüst:** több táblát kapcsol, aggregál, és meg tudja indokolni az `INNER`/`LEFT JOIN` választását.
- **Arany:** CTE-t, ablakfüggvényt, megszorításokat és tranzakciót is helyesen használ.
- **Projektkész:** új domaint tud modellezni, és a lekérdezéseit elvárt eredménnyel teszteli.

## Mesteri ellenőrző kérdések

1. Mi a lekérdezés grainje, és hol változik meg a JOIN miatt?
2. Miért lehet hibás a `NOT IN`, ha NULL is előfordul?
3. Mikor kell `WHERE`, és mikor `HAVING`?
4. Miért nem bizonyítja a helyes eredmény önmagában a jó teljesítményt?
5. Mitől lesz egy módosítás visszagörgethető és újrafuttatható?

Ha valamelyikre nem tudsz válaszolni, térj vissza a kapcsolódó `content/` cikkhez, majd írj egy saját, kicsi példát.
