# Oktatói útmutató

## Ajánlott használat

Egy 90 perces alkalom felosztása: 10 perc előhívó kérdések, 15 perc magyarázat, 20 perc közös kódolás, 30 perc önálló feladat, 10 perc közös hibakeresés, 5 perc kilépőkártya.

Az oktató ne a megoldást vetítse ki elsőként. Kérdezze meg: mi a kívánt grain, melyik tábla a forrás, lehet-e NULL vagy duplikáció, és hogyan ellenőrizhető az eredmény.

## Differenciálás

- Kezdőnek: használja a közös sémát, és adjon egyetlen táblás feladatot.
- Haladónak: kérjen alternatív megoldást (`JOIN` és `EXISTS`), majd hasonlítsa össze a szemantikát.
- Erős tanulónak: kérjen vendor-specifikus változatot és execution-plan indoklást.

## Értékelési rubrika

| Szempont | 0 pont | 1 pont | 2 pont |
|---|---|---|---|
| Szemantika | nem válaszolja meg a kérdést | részben helyes | pontos result set |
| Grain és JOIN | nem azonosítja | működik, de indoklás nélkül | helyesen indokolja |
| NULL/duplikáció | figyelmen kívül hagyja | felismeri | teszttel bizonyítja |
| Olvashatóság | nehezen követhető | elfogadható | jól nevezett, tagolt SQL |
| Biztonság | veszélyes módosítás | részleges védelem | ellenőrzés + tranzakció |

## Kilépőkártya

Minden alkalom végén a tanuló írja le: egy fogalom, amit megértett; egy hiba, amit elkövetett; és egy kérdés, amit a következő alkalommal meg akar oldani.
