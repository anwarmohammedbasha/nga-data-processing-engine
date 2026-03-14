-- Active: 1773376467237@@bbhyufmayffhtdiehvvakkry7m.wrgcbhi-vr00936.ap-southeast-1.aws.postgres.snowflake.app@5432@nga_dev
CREATE TABLE NGA_CUSTOMER_TBL (
    customer_id VARCHAR PRIMARY KEY,
    store_name VARCHAR,
    contact_person VARCHAR,
    city VARCHAR,
    state VARCHAR,
    address VARCHAR,
    pincode VARCHAR,
    mobile_number VARCHAR,
    gst_number VARCHAR,
    customer_type VARCHAR
);

SELECT * FROM NGA_CUSTOMER_TBL;

TRUNCATE TABLE NGA_CUSTOMER_TBL