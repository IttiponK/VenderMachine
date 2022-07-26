from typing import Optional
from pydantic import BaseModel

class Order(BaseModel):
    name:Optional[str]
    product_id:Optional[str]
    pay_amount:Optional[int]
    pay_amount_detail:Optional[dict]
    quantity:Optional[int]