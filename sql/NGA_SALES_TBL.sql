CREATE TABLE IF NOT EXISTS public.nga_sales_tbl (
    invoice_id VARCHAR(50) PRIMARY KEY,
    order_date DATE,
    customer_id VARCHAR(50),
    product_id VARCHAR(50),
    order_quantity_boxes INTEGER,
    billed_quantity_boxes INTEGER,
    price_per_box_at_sale NUMERIC(12, 2),
    tax_percentage NUMERIC(5, 2),
    discount_percentage NUMERIC(5, 2),
    line_total_before_tax_discount NUMERIC(12, 2),
    tax_amount NUMERIC(12, 2),
    discount_amount NUMERIC(12, 2),
    final_line_total NUMERIC(12, 2),
    payment_status VARCHAR(20),
    delivery_status VARCHAR(20)
);

TRUNCATE TABLE public.nga_sales_tbl;