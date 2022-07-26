from abc import ABC,abstractmethod
from ..domain.base.aggregate import AggregateBase

class DBPort(ABC):
    
    @abstractmethod
    def create_new_transaction(self,name,product_id,quantity,total_amount,pay_amount,pay_amount_detail,change,change_detail) -> bool:
        pass 
    