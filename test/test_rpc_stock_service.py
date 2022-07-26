from stockservice.hexagonalmodel.domain import usecase 
from stockservice.hexagonalmodel.domain.registry import Registry
from stockservice.hexagonalmodel.adapter.inmemory import InmemoryDB
from stockservice.hexagonalmodel.domain.model.stock import Stock

test_dependency = InmemoryDB(Stock)

def test_should_return_True_when_product_id_is_correct_and_quantity_equal_or_more():
    Registry().stock = test_dependency
    status,price = usecase.product_is_already('test1',2)
    assert status == True 
    
def test_should_return_False_when_product_id_is_incorrect():
    Registry().stock = test_dependency
    status,price = usecase.product_is_already('invalidproduct_id',2)
    assert status == False
    
def test_should_return_False_when_product_id_is_correct_and_quantity_more_than_product_quantity():
    Registry().stock = test_dependency
    status,price = usecase.product_is_already('invalidproduct_id',200)
    assert status == False
    
def test_should_return_False_when_update_product_raise_InvalidUpdate():
    Registry().stock = InmemoryDB(Stock,False)
    purchaseStatus = usecase.update_product('validproduct_id',2)
    assert purchaseStatus == False
    
def test_shoul_return_True_when_update_product_not_raise_InvalidUpdate():
    Registry().stock = InmemoryDB(Stock,True)
    purchaseStatus = usecase.update_product('validproduct_id',2)
    assert purchaseStatus == True
        
    