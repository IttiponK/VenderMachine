from ..domain.base.exception import InvalidUpdate
from ..port.db import DBPort 

class InmemoryDB(DBPort):
    def __init__(self,model,updateStatus=True):
        self.model = model 
        self.products = [
            {'product_id':'test1','name':'test','price':300,'quantity':2,'img':'https://test.img','version':0},
            {'product_id':'test2','name':'test','price':300,'quantity':2,'img':'https://test.img','version':0},
            {'product_id':'test3','name':'test','price':300,'quantity':2,'img':'https://test.img','version':0},
            {'product_id':'test4','name':'test','price':300,'quantity':2,'img':'https://test.img','version':0},
            {'product_id':'test5','name':'test','price':300,'quantity':2,'img':'https://test.img','version':0},
            {'product_id':'test6','name':'test','price':300,'quantity':2,'img':'https://test.img','version':0},
        ]
        self.updateStatus = updateStatus
        
    def all(self) -> list:
        fakedata = self.products
        result = [self.model(**data).serializerProductDetails() for data in fakedata]
        return result
    
    def product_is_already(self, product_id, quantity) :
        for product in self.products:
            if product.get('product_id') == product_id and product.get('quantity') >= quantity:
                return [True , product.get('price')]
        return [False ,0]
    
    def update_product(self, product_id, quantity) -> bool:
        if self.updateStatus:
            return True 
        raise InvalidUpdate