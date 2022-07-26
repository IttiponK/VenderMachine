from nameko.rpc import rpc 
from ..hexagonalmodel.domain.registry import Registry
from ..hexagonalmodel.adapter.mysqlinsqlalchemy import MySQLinSQLAlchemy
from ..hexagonalmodel.domain.model.cashbag import CashBag
from ..hexagonalmodel.domain import usecase

Registry().cashbag = MySQLinSQLAlchemy(CashBag)


class Service:
    name = 'vending'
    
    @rpc
    def change_process(self,pay_amount,totalprice):
        changeStatus,change,changeDetail = usecase.get_changeStatus_and_changeDetail(pay_amount,totalprice)
        return changeStatus,change,changeDetail
    
    @rpc 
    def update_cash(self,cashObjupdate):
        usecase.update_cash(cashObjupdate)
        return 