from ..port.db import DBPort 
from sqlalchemy.orm import Session
from ..domain.base.aggregate import AggregateBase
from ...infrastructure.mysql.connect import connect_mysql_db


class MySQLinSQLAlchemy(DBPort):
    def __init__(self,model):
        connect,cashbag = connect_mysql_db()
        self.connect = connect 
        self.cashbag = cashbag 
        self.model:AggregateBase = model
        
    def get_all_cash(self) -> list:
        db:Session = next(self.connect())
        cashBag = db.query(self.cashbag).filter_by(active = 1)\
            .filter(self.cashbag.quantity > 0).order_by(self.cashbag.value.desc()).all()
        listcashBag = [self.model.from_orm(cash).to_cashlist() for cash in cashBag]
        return listcashBag
    
    def update_from_dict(self, changeObjupdate:dict):
        db:Session = next(self.connect())
        for value,quantity in changeObjupdate.items():
            db.query(self.cashbag).filter_by(value=value)\
                .filter(self.cashbag.active == 1).update({'quantity':self.cashbag.quantity - quantity})
        
        db.commit()
            
        