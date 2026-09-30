WITH RECURSIVE tree AS (SELECT employee_id, name, manager_id, 0 AS depth FROM employees WHERE manager_id IS NULL UNION ALL SELECT e.employee_id, e.name, e.manager_id, t.depth + 1 FROM employees e JOIN tree t ON e.manager_id = t.employee_id) SELECT employee_id, name, depth FROM tree ORDER BY depth, employee_id;
SELECT manager_id, COUNT(*) AS direct_reports FROM employees WHERE manager_id IS NOT NULL GROUP BY manager_id;
-- Productionban depth limit, visited-id lista vagy engine-specifikus CYCLE kezelés szükséges.
