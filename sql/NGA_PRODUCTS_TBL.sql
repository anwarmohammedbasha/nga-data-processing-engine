CREATE TABLE NGA_PRODUCTS_TBL (
    product_id VARCHAR PRIMARY KEY,
    product_name VARCHAR, 
    brand VARCHAR,
    category VARCHAR,
    origin VARCHAR,
    price_per_unit FLOAT,
    units_per_box FLOAT,
    price_per_box FLOAT
);

DROP TABLE NGA_PRODUCTS_TBL