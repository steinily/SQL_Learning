-- query: NULL pótlása
SELECT c.name, COALESCE(o.status, 'nincs rendelés') AS order_status FROM customers AS c LEFT JOIN orders AS o ON o.customer_id = c.customer_id ORDER BY c.name, o.order_id;
-- query: tényleges kapcsolt sorok számlálása
SELECT c.name, COUNT(o.order_id) AS order_count FROM customers AS c LEFT JOIN orders AS o ON o.customer_id = c.customer_id GROUP BY c.customer_id, c.name ORDER BY c.name;
