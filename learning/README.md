# Gyakorlólabor

A labor közös adatmodellje egy kis webshop: `customers`, `products`, `orders` és `order_items`. A modell tartalmaz egy-a-többhöz és több-a-többhöz kapcsolatot, státuszokat és összegezhető mennyiségeket.

```bash
python3 scripts/learning_runner.py
python3 scripts/learning_runner.py --lesson 2
python3 scripts/learning_runner.py --list
```

A runner minden futáskor új memóriabeli SQLite adatbázissal indul. A feladatokat a `learning/exercises/` könyvtárban oldd meg; a mintamegoldásokat csak utána nyisd meg.

Részletes feladatmenet: [exercises/README.md](exercises/README.md). A labor tanulási célra készült; production SQL előtt mindig ellenőrizd a cél-adatbázis dialectjét és verzióját.
