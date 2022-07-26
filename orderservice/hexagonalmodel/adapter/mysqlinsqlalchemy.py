from ..port.db import DBPort 
from sqlalchemy.orm import Session
from ..domain.base.aggregate import AggregateBase

class MySQLinSQLAlchemy(DBPort):
    def __init__(self,connect,transaction):
        self.connect = connect
        self.transaction = transaction
    
    # def save_to_db(self, data: AggregateBase):
    #     db:Session = next(self.connect())
    #     newTransaction = self.transaction(**data.dict())
    #     try:
    #         db.add(newTransaction)
    #         db.commit()
    #     except:
    #         db.rollback()
    
    def create_new_transaction(self, name, product_id, quantity, total_amount, pay_amount, pay_amount_detail, change, change_detail) -> bool:
        data = {
            'name':name,
            'product_id':product_id,
            'quantity':quantity,
            'total_amount':total_amount,
            'pay_amount':pay_amount,
            'pay_amount_detail':pay_amount_detail,
            'change':change,
            'change_detail':change_detail
        }        
        db:Session = next(self.connect())
        newTransaction = self.transaction(**data)
        
        db.add(newTransaction)
        db.commit()

            