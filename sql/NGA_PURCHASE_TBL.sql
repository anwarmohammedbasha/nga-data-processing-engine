-- Active: 1773376467237@@bbhyufmayffhtdiehvvakkry7m.wrgcbhi-vr00936.ap-southeast-1.aws.postgres.snowflake.app@5432@nga_dev
CREATE TABLE NGA_PURCHASE_TBL (
    purchase_id VARCHAR PRIMARY KEY,
    purchase_date VARCHAR,
    product_id VARCHAR,
    supplier_name VARCHAR,
    quantity_boxes integer,
    cost_per_box float,
    total_purchase_cost float,
    payment_terms VARCHAR,
    country VARCHAR,
    customs_duties float
);

DROP TABLE NGA_PRODUCTS_TBL