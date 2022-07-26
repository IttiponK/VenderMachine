from ..port.db import DBPort 

class InmemoryDB(DBPort):
    def __init__(self):
        self.db = []
    
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
        self.db.append(data)