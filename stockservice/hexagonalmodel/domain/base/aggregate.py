from pydantic import BaseModel
from datetime import datetime
from abc import ABC,abstractmethod
import secrets

class AggregateBase(BaseModel):
    id:int = None
    name:str = None
    product_id:str = secrets.token_urlsafe()[:20]
    quantity:int = None
    price:int = None
    img:str = None
    version:int = None 
    create_at:datetime = None
    
    class Config:
        orm_mode = True
        
    @abstractmethod
    def serializerProductDetails(self) -> dict:
        pass 