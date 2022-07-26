from .base.exception import InvalidUpdate
from .registry import Registry 

def get_all_products() -> list:
    repo = Registry()
    products = repo.stock.all()
    return products

def product_is_already(product_id:str,quantity:int):
    repo = Registry()
    status,price = repo.stock.product_is_already(product_id,quantity)
    return status,price 

def update_product(product_id:str,quantity:int) ->bool:
    repo = Registry() 
    try:
        status = repo.stock.update_product(product_id,quantity)
        return status
    except InvalidUpdate:
        return False