from ..base.aggregate import AggregateBase 

class CashBag(AggregateBase):
    
    def to_cashlist(self) -> list:
        return (self.value,self.quantity)