from ..port.db import DBPort 

class InmemoryDB(DBPort):
    def __init__(self,cashbag:dict):
        self.cashbag = cashbag
    
    def get_all_cash(self) -> list:
        return self.cashbag
    
    def update_from_dict(self, changeObjupdate: dict):
        pass 