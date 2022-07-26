from nameko.rpc import rpc 
from ..hexagonalmodel.domain import usecase
from ..hexagonalmodel.domain.registry import Registry
from ..hexagonalmodel.domain.model.stock import Stock
from ..hexagonalmodel.adapter.mysqlinsqlalchemy import MySQLinSQLAlchemy

Registry().stock = MySQLinSQLAlchemy(Stock)


class Service:
    name = 'stock'
    
    @rpc
    def check_product_status(self,product_id,quantity):
        status,price = usecase.product_is_already(product_id,quantity)
        
        return status,price 
    
    @rpc 
    def purchase(self,product_id,quantity):
        purchaseStatus = usecase.update_product(product_id,quantity)
        return purchaseStatus
    
    
    