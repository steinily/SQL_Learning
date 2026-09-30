# 14. Rekurzív CTE

## Cél

Járj be hierarchikus adatot rekurzív CTE-vel, és értsd meg, miért kell a ciklusokra és a maximális mélységre védelem.

```sql
WITH RECURSIVE tree AS (
    SELECT employee_id, name, manager_id, 0 AS depth
    FROM employees WHERE manager_id IS NULL
    UNION ALL
    SELECT e.employee_id, e.name, e.manager_id, t.depth + 1
    FROM employees e JOIN tree t ON e.manager_id = t.employee_id
)
SELECT * FROM tree ORDER BY depth, employee_id;
```

Az anchor rész indítja a bejárást, a recursive rész újabb sorokat ad hozzá. Production rendszerben gondolj ciklusvédelemre, depth limitre és indexre a kapcsoló oszlopokon.

## Gyakorlat

Oldd meg a [`14-recursive.sql`](../exercises/14-recursive.sql) feladatot, majd futtasd a `python3 scripts/learning_runner.py --lesson 12` demót.
