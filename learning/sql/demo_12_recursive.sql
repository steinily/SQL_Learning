-- query: hierarchia létrehozása
CREATE TABLE employees (employee_id INTEGER PRIMARY KEY, name TEXT NOT NULL, manager_id INTEGER REFERENCES employees(employee_id));
-- query: hierarchia feltöltése
INSERT INTO employees VALUES (1, 'Igazgató', NULL), (2, 'Elemző vezető', 1), (3, 'Adatbázis-adminisztrátor', 1), (4, 'Junior elemző', 2), (5, 'Riportkészítő', 2);
-- query: hierarchia bejárása
WITH RECURSIVE tree AS (SELECT employee_id, name, manager_id, 0 AS depth FROM employees WHERE manager_id IS NULL UNION ALL SELECT e.employee_id, e.name, e.manager_id, t.depth + 1 FROM employees e JOIN tree t ON e.manager_id = t.employee_id) SELECT employee_id, name, depth FROM tree ORDER BY depth, employee_id;
