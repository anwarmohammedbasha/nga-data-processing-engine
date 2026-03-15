from pydantic import BaseModel
from datetime import date
from typing import Optional

class Sales(BaseModel):
    invoice_id: str
    order_date: date
    customer_id: str
    product_id: str
    order_quantity_boxes: int
    billed_quantity_boxes: int
    price_per_box_at_sale: float
    tax_percentage: float
    discount_percentage: float
    line_total_before_tax_discount: float
    tax_amount: float
    discount_amount: float
    final_line_total: float
    payment_status: str
    delivery_status: str