# Locking mintamegoldás

1. Blockingnál az egyik tranzakció vár a másik által tartott lockra; deadlocknál a tranzakciók körben várnak egymásra.
2. Rövid tranzakció, megfelelő index, stabil erőforrás-sorrend, alacsony lockolt sorhalmaz és retryable timeout-kezelés csökkenti a kockázatot.
3. A pontos isolation level és lock mode mindig a használt adatbázis-engine dokumentációja szerint ellenőrizendő.
