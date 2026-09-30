# SQL Learning

Tanulási célú SQL-repozitórium magyar magyarázatokkal, futtatható példákkal és ellenőrizhető gyakorlatokkal.

## Hol kezdjem?

Ha most tanulod az SQL-t, először klónozd a repót, majd kövesd a [tanulási útvonalat](LEARNING_PATH.md):

```bash
git clone https://github.com/steinily/SQL_Learning.git
cd SQL_Learning
python3 scripts/learning_runner.py
```

Az alaplaborhoz Python 3.10+ szükséges; nincs szükség adatbázis-szerverre vagy külső Python-csomagra. Minden futás izolált, ideiglenes SQLite adatbázist épít fel.

## Az első 30 perc

1. Olvasd el a [0. leckét](learning/lessons/00-kornyezet.md), majd futtasd a `python3 scripts/learning_runner.py --lesson 1` parancsot.
2. Oldd meg az [1. feladatsort](learning/exercises/01-select.sql) a saját `my-answer.sql` fájlodban.
3. Futtasd a saját fájlodat: `python3 scripts/learning_runner.py --file my-answer.sql`.
4. Csak ezután nézd meg a [mintamegoldást](learning/solutions/01-select.sql).

## Mit tartalmaz?

- `learning/lessons/` — 12 lépéses vezetett útvonal (0–11): cél, előfeltétel, magyarázat, kód és ellenőrző kérdések;
- `learning/exercises/` — önállóan megoldandó feladatok;
- `learning/solutions/` — mintamegoldások, csak a feladat megkísérlése után;
- `learning/ASSESSMENT.md` — önellenőrző kérdések és haladási szintek;
- `INSTRUCTOR_GUIDE.md` — óraterv, differenciálás és értékelési rubrika;
- `learning/sql/` — közös, kis webshop-adatmodell és demo lekérdezések;
- `content/` — a részletes, kereshető referenciaanyag 36 tématerületen;
- `scripts/learning_runner.py` — telepítésmentes gyakorlófuttató;
- `tests/` és `Makefile` — a repó minőségi ellenőrzése.

A feladatok részletes munkamenete a [learning/exercises/README.md](learning/exercises/README.md) fájlban található.

## Fontos: SQLite és production SQL

Az alapleckék SQLite-on futnak, hogy bárki azonnal elkezdhessen gyakorolni. Ez nem jelenti azt, hogy minden példa minden adatbázisban azonosan működik: a típusrendszer, dátumfüggvények, JSON, `LIMIT`/`TOP`, tranzakciós és locking-viselkedés eltérhet. Production használat előtt mindig ellenőrizd a célrendszer dialectjét és verzióját.

## Tanulási modell

Minden leckénél ezt a ciklust kövesd: olvasd el a célt, futtasd a példát, módosítsd a lekérdezést, oldd meg a feladatot, majd hasonlítsd össze a mintamegoldással.

## A referenciaanyag használata

A `content/` könyvtár nem kötelezően lineáris tankönyv, hanem fogalmi referencia. A tanulási útvonal minden szakaszán megadja, melyik részletes cikket érdemes elolvasni. Az alapleckék portable SQL/SQLite példákat használnak; a vendor-specifikus eltéréseket külön jelöljük.

## Ellenőrzés

```bash
make learn
make test
make validate
```

Az első parancs a tanulói labort futtatja. A `make test` és `make validate` fejlesztői ellenőrzéshez a `requirements-dev.txt` csomagjait használja; ezek nem szükségesek a tanuláshoz.

Fejlesztői ellenőrzéshez először telepítsd a csomagokat:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
make test
make validate
```

Új leckéhez használd a [közreműködési útmutatót](CONTRIBUTING.md). A cél: minden új fogalomhoz legyen rövid magyarázat, futtatható példa, gyakorlófeladat és egyértelmű elvárt eredmény.
