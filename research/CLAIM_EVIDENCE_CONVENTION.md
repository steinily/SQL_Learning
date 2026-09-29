# Claim and Evidence Convention

## Cél

A technikai állítás csak akkor kerülhet canonical dokumentumba ellenőrzöttként, ha a hozzá
tartozó research package `claims` bejegyzése megnevezi az evidence levelt, a source ID-kat,
az alkalmazási kontextust és az állapotot. A URL önmagában nem bizonyíték.

## Állapotok

- `VERIFIED`: a hivatkozott forrás közvetlenül alátámasztja az állítást.
- `VERIFY_REQUIRED`: nincs elég közvetlen bizonyíték.
- `SOURCE_CONFLICT`: hiteles források eltérnek; az eltérés nincs feloldva.
- `VERSION_UNCONFIRMED`: a viselkedés verziófüggő, de a verzió nincs igazolva.
- `EXECUTION_NOT_TESTED`: reprodukció indokolt, de tényleges futtatás nem történt.

`E1` dokumentumszintű authoritative hivatkozást, `E2` állításszintű bizonyítékot,
`E3` pedig reprodukciót igénylő viselkedési vagy performance állítást jelöl. A Writer nem
módosíthatja saját munkáját `fully-verified` állapotúra; ehhez külön Validation és Audit
pass szükséges.

## Frissesség és verzió

A source record tartalmazza a lekérés dátumát, az érintett technology/version kontextust,
és szükség esetén a `review_after` dátumot. Current vendor behavior esetén az official
dokumentáció vagy release note elsődleges; bizonytalan eredmény explicit uncertainty
állapotban marad.
