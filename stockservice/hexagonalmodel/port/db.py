from abc import ABC,abstractmethod
from typing import List

class DBPort(ABC):
    
    @abstractmethod
    def all(self) -> list:
        pass 
    
    @abstractmethod
    def product_is_already(self,product_id,quantity) :
        pass 
    
    @abstractmethod
    def update_product(self,product_id,quantity) -> bool:
        pass 
    
    