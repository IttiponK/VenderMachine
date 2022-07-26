
from ...rest.requestmodel import Order
from ..domain.registry import Registry
from ..domain.base.exception import (
    CashNotEnough,
    PayAmountNotLessthantotalprice,
    ProductIsnotAlready,
    PurchaseNotsuccess
    )
from ..domain.model import mergedict

def create_order(order:Order):
    with Registry().rpc as rpc:
        # productStatus,price = rpc.stock.check_product_status(order.product_id,order.quantity)
        # if productStatus:
        #     totalprice = price * order.quantity
        #     if order.pay_amount >= totalprice:
        #         changeStatus,change,changeDetail = rpc.vending.change_process(order.pay_amount,totalprice)
        #         if changeStatus:
        #             purchaseStatus = rpc.stock.purchase(order.product_id,order.quantity)
        #             if purchaseStatus:
        #                 cashObjupdate = mergedict.merge(changeDetail,order.pay_amount_detail)
        #                 rpc.vending.update_cash(cashObjupdate)
        #                 Registry().transaction.create_new_transaction(
        #                     name=order.name,
        #                     product_id=order.product_id,
        #                     quantity=order.quantity,
        #                     total_amount=totalprice,
        #                     pay_amount=order.pay_amount,
        #                     pay_amount_detail=str(order.pay_amount_detail),
        #                     change=change,
        #                     change_detail=str(changeDetail)
        #                 )
        #                 return ['success',changeDetail]
        #             raise PurchaseNotsuccess
        #         raise CashNotEnough
        #     raise PayAmountNotLessthantotalprice
        # raise ProductIsnotAlready
        price = get_price(rpc,order.product_id,order.quantity)
        totalprice = price * order.quantity
        if can_pay(order.pay_amount,totalprice):
            change,changeDetail = change_process(rpc,order.pay_amount,totalprice)
            if can_purchase(rpc,order.product_id,order.quantity):
                cashObjupdate = mergedict.merge(changeDetail,order.pay_amount_detail)
                update_cash(rpc,cashObjupdate)
                create_new_transaction(
                    name=order.name,
                    product_id=order.product_id,
                    quantity=order.quantity,
                    totalprice=totalprice,
                    pay_amount=order.pay_amount,
                    pay_amount_detail=order.pay_amount_detail,
                    change=change,
                    changeDetail=changeDetail
                )
            return ['success',changeDetail]

def get_price(rpc,product_id,quantity):
    productStatus,price = rpc.stock.check_product_status(product_id,quantity)
    if productStatus:
        return price
    raise ProductIsnotAlready

def can_pay(pay_amout,totalprice):
    if pay_amout < totalprice:
        raise PayAmountNotLessthantotalprice
    return True 
    
def change_process(rpc,pay_amount,totalprice):
    changeStatus,change,changeDetail = rpc.vending.change_process(pay_amount,totalprice)
    if changeStatus:
        return change,changeDetail
    raise CashNotEnough

def can_purchase(rpc,product_id,quantity):
    purchaseStatus = rpc.stock.purchase(product_id,quantity)
    if not purchaseStatus:
        raise PurchaseNotsuccess
    return purchaseStatus
    
def update_cash(rpc,cashObjupdate):
    rpc.vending.update_cash(cashObjupdate)
    
def create_new_transaction(name,product_id,quantity,totalprice,pay_amount,pay_amount_detail,change,changeDetail):
    Registry().transaction.create_new_transaction(
            name=name,
            product_id=product_id,
            quantity=quantity,
            total_amount=totalprice,
            pay_amount=pay_amount,
            pay_amount_detail=str(pay_amount_detail),
            change=change,
            change_detail=str(changeDetail)
        )
    
        
        
