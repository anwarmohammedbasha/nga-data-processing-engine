from pydantic import BaseModel

class Products(BaseModel):
    product_id: str
    product_name: str
    brand: str
    category: str
    origin: str
    price_per_unit: float
    units_per_box: float
    price_per_box: float