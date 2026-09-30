# 0. A környezet és az adatmodell

## Cél

Meg tudd különböztetni az adatbázist, a táblát, a sort, az oszlopot és a kulcsot. A labor SQLite-ot használ, mert külön szerver nélkül futtatható.

## A webshop modellje

- `customers`: vevők;
- `products`: termékek;
- `orders`: rendelések;
- `order_items`: a rendelés és termék közötti kapcsolat, mennyiséggel.

Az `orders.customer_id` külső kulcs (`foreign key`), az `order_items` összetett elsődleges kulcsa pedig megakadályozza, hogy ugyanaz a termék kétszer szerepeljen egy rendelésben.

## Próbáld ki

```bash
python3 scripts/learning_runner.py --list
python3 scripts/learning_runner.py --lesson 1
```

## Ellenőrző kérdések

1. Miért nem tároljuk a vevő nevét minden rendelési sorban?
2. Melyik tábla oldja fel a rendelés–termék több-a-többhöz kapcsolatot?

Következő: [01 — Lekérdezés](01-lekerdezes.md).
