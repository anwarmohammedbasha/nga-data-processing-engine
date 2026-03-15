from pydantic import BaseModel
from datetime import date

class Purchase(BaseModel):
    purchase_id: str
    purchase_date: str
    product_id: str
    supplier_name: str
    quantity_boxes: int
    cost_per_box: float
    total_purchase_cost: float
    payment_terms: str
    country: str
    customs_duties: float