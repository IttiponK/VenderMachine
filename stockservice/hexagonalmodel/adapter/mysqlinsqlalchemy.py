from ..domain.base.exception import InvalidUpdate
from ..domain.base.aggregate import AggregateBase
from ..port.db import DBPort 
from sqlalchemy.orm import Session 
from ...infrastructure.mysql.connect import connect_mysql_db

class MySQLinSQLAlchemy(DBPort):
    def __init__(self,model):
        connect,stock = connect_mysql_db()
        self.connect = connect 
        self.stock = stock 
        self.model:AggregateBase = model
        
    def all(self) -> list:
        db:Session = next(self.connect())
        products = db.query(self.stock).filter(self.stock.quantity > 0).all()
        result = [self.model.from_orm(product).serializerProductDetails() for product in products]
        return result
    
    def product_is_already(self, product_id, quantity):
        db:Session = next(self.connect())
        product = db.query(self.stock).filter_by(product_id = product_id) \
            .filter(self.stock.quantity >= quantity).first()
        if product:
            return [True ,product.price]
        return [False , 0 ]
    
    def update_product(self, product_id, quantity) -> bool:
        db:Session = next(self.connect())
        try:
            db.query(self.stock).filter_by(product_id = product_id) \
                .filter(self.stock.quantity >= quantity) \
                .update({'quantity':self.stock.quantity - quantity})
            db.commit()
            return True 
        except:
            db.rollback()
            raise InvalidUpdate
    
    