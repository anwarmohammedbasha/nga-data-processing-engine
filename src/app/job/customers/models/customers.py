from pydantic import BaseModel

class Customers(BaseModel):
    customer_id: str
    store_name: str
    contact_person: str
    city: str
    state: str
    address: str
    pincode: int
    mobile_number: int
    gst_number: str
    customer_type: str