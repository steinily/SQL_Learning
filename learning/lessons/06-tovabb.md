# 6. Hogyan folytasd?

A kezdő útvonal után válassz fókuszt: adatmodellezés, PostgreSQL/SQL Server/MySQL, indexelés és execution plan, tranzakciók, vagy analitikai SQL.

## Ellenőrzőpont

Ne lépj tovább pusztán azért, mert lefut a lekérdezés. Akkor állsz készen, ha meg tudod magyarázni a result set alakját, az esetleges duplikációkat, a NULL viselkedését és azt, hogy mikor változik a megoldás egy másik SQL-dialektusban.

Használd a [36 modult tartalmazó manifestet](../../manifest/v1.yaml) és a `content/` könyvtárban az adott témához tartozó overview cikket. Minden vendor-specifikus példát a célrendszeren futtass, mert a portable SQL és a konkrét dialect nem ugyanaz.

## Záró projekt

Válassz egy kis domaint (könyvtár, sportklub vagy rendeléskezelés), készíts legalább négy táblát kulcsokkal és megszorításokkal, töltsd fel tesztadattal, majd írj öt üzleti lekérdezést: egyszerű listázás, JOIN, aggregáció, CTE és ablakfüggvény.

A projekt értékelési szempontjai: helyes grain, kulcsok és megszorítások (30%), olvasható és helyes SQL (30%), tesztadat és ellenőrizhető eredmény (20%), magyarázat és trade-offok (20%).
