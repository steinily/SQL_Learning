WITH ranked AS (SELECT p.*, ROW_NUMBER() OVER (PARTITION BY category ORDER BY unit_price DESC, product_id) AS position FROM products p) SELECT name, category, unit_price FROM ranked WHERE position = 1;
WITH ranked AS (SELECT p.*, ROW_NUMBER() OVER (PARTITION BY category ORDER BY unit_price DESC, product_id) AS position FROM products p) SELECT name, category, unit_price FROM ranked WHERE position <= 2;
-- RANK esetén azonos értékek azonos helyezést kapnak, és több mint N sor is visszatérhet.
