-- query: átlagár feletti termékek
SELECT name, unit_price FROM products WHERE unit_price > (SELECT AVG(unit_price) FROM products) ORDER BY unit_price;
-- query: legalább egy fizetett rendelést leadó vevők
SELECT c.name FROM customers AS c WHERE EXISTS (SELECT 1 FROM orders AS o WHERE o.customer_id = c.customer_id AND o.status = 'paid') ORDER BY c.name;
