# 18. Haladó projekt

## Feladat

Válassz egy legalább 100 000 soros, vagy generáltan skálázható domain-adatkészletet. Készíts két üzleti lekérdezést, amelyek közül az egyik window functiont vagy rekurzív CTE-t használ, a másik pedig aggregál.

Mérd meg a lekérdezéseket index nélkül és indexszel, mentsd el a terveket, és írd le:

1. mi a query grainje;
2. mely predicate-ek sargable-ek;
3. milyen cardinality-becslést vársz;
4. miért választottál vagy utasítottál el egy indexet;
5. milyen locking/isolation kockázat marad.

## Leadandó anyag

Használd a [`18-advanced-project.md`](../exercises/18-advanced-project.md) sablont. A projektet az oktató az eredményhelyesség, mérési bizonyíték, indexindoklás, concurrency-gondolkodás és magyarázat alapján értékelje.
