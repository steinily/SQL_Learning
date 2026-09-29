PRAGMA foreign_keys = ON;

CREATE TABLE organization (
    organization_id INTEGER PRIMARY KEY,
    organization_code VARCHAR(20) NOT NULL UNIQUE,
    organization_name VARCHAR(200) NOT NULL
);

CREATE TABLE customer (
    customer_id INTEGER PRIMARY KEY,
    organization_id INTEGER NOT NULL,
    customer_code VARCHAR(20) NOT NULL UNIQUE,
    customer_name VARCHAR(200) NOT NULL,
    country_code CHAR(2) NOT NULL,
    FOREIGN KEY (organization_id) REFERENCES organization (organization_id)
);

CREATE TABLE product (
    product_id INTEGER PRIMARY KEY,
    sku VARCHAR(30) NOT NULL UNIQUE,
    product_name VARCHAR(200) NOT NULL,
    unit_price DECIMAL(12, 2) NOT NULL CHECK (unit_price >= 0)
);

CREATE TABLE sales_order (
    sales_order_id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    ordered_at TIMESTAMP NOT NULL,
    status VARCHAR(20) NOT NULL CHECK (status IN ('NEW', 'CONFIRMED', 'SHIPPED', 'CANCELLED')),
    FOREIGN KEY (customer_id) REFERENCES customer (customer_id)
);

CREATE TABLE sales_order_line (
    sales_order_id INTEGER NOT NULL,
    line_number INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    unit_price DECIMAL(12, 2) NOT NULL CHECK (unit_price >= 0),
    PRIMARY KEY (sales_order_id, line_number),
    FOREIGN KEY (sales_order_id) REFERENCES sales_order (sales_order_id),
    FOREIGN KEY (product_id) REFERENCES product (product_id)
);
