-- query: alap lekérdezés
SELECT product_id, name, unit_price FROM products WHERE unit_price >= 5000 ORDER BY unit_price DESC;
-- query: rendezett, korlátozott lista
SELECT name, category FROM products ORDER BY name LIMIT 3;
