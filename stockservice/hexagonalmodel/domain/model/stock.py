from ..base.aggregate import AggregateBase

class Stock(AggregateBase):
    
    def serializerProductDetails(self) -> dict:
        data = self.dict() 
        del data['version']
        return data