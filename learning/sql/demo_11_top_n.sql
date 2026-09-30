-- query: kategóriánként a két legdrágább termék
WITH ranked AS (SELECT p.*, ROW_NUMBER() OVER (PARTITION BY category ORDER BY unit_price DESC, product_id) AS position FROM products p) SELECT name, category, unit_price, position FROM ranked WHERE position <= 2 ORDER BY category, position;
