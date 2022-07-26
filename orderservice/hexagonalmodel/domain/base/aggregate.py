from pydantic import BaseModel
from datetime import datetime


class AggregateBase(BaseModel):
    id:int = None
    name:str
    porduct_id:str
    quantity:int 
    total_amount:int 
    pay_amount:int 
    pay_amount_detail:str 
    change:int 
    change_detail:str 
    to:str 
    create_at:datetime = None