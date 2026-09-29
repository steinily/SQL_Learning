# Engine adapters

A `canonical/schema.sql` a kis, engine-neutral teaching model. Az explicit integer key és
timestamp/value input gondoskodik a determinisztikus fixture-ről. Vendor adapter csak ott
engedélyezett, ahol a DDL vagy a viselkedés ténylegesen eltér; a canonical entity modelt nem
duplikálhatja és nem változtathatja meg.

Az első executable adapter `sqlite-local`, kizárólag portable/local ellenőrzéshez. A
PostgreSQL és SQL Server primary, valamint MySQL secondary adapter állapota az
`examples/environments.yaml` fájlban látható; nem elérhető környezet `NOT_RUN`, nem `PASS`.
