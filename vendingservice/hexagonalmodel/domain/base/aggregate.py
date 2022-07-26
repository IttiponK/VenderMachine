from datetime import datetime
from pydantic import BaseModel
from abc import ABC,abstractmethod

class AggregateBase(BaseModel,ABC):
    id:int = None
    value:int = None 
    quantity:int = None 
    active: int = None 
    create_at: datetime = None
    
    class Config:
        orm_mode = True
    
    @abstractmethod
    def to_cashlist(self) -> list:
        pass 
    
    