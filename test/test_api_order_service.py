from orderservice.rest.initapp import create_app 
from fastapi.testclient import TestClient
from orderservice.hexagonalmodel.domain.registry import Registry
from pytest import raises
from orderservice.hexagonalmodel.adapter.inmemory import InmemoryDB

class MockStockRpc:   
    def __init__(self,product_status,price,purchaseStatus=True):
        self.product_status = product_status
        self.price = price
        self.purchanseStatus = purchaseStatus

    def check_product_status(self,product_id,quantity):
        return self.product_status,self.price
    
    def purchase(self,product_id,quantity):
        return self.purchanseStatus
    
class MockVendingMachineRpc:
    def __init__(self,changeStatus,change,changeDetails):
        self.changeStatus = changeStatus
        self.change = change 
        self.changeDetails = changeDetails
        
    def change_process(self,pay_amount,totalprice):
        return self.changeStatus,self.change,self.changeDetails
    
    def update_cash(self,cashObjupdate):
        pass 

class MockRPC:
    def __init__(self,stock,vending=None):
        self.stock = stock
        self.vending = vending
        
    def __enter__(self):
        return self 
    
    def __exit__(self,a,b,c):
        pass 

client = TestClient(create_app())


def test_should_return_message_product_is_not_already_when_quantity_is_more_than_product_quantity():
    mockstock = MockStockRpc(False,0)
    mockrpc = MockRPC(mockstock)
    Registry().rpc = mockrpc
    data = {
        "product_id": "test123",
        "pay_amount": 0,
        "pay_amount_detail": {100:1},
        "quantity": 200
        }
    response = client.post('/api/v1/create_order',json=data)
    assert response.json().get('message') == 'Product is not already' 
    assert response.status_code == 406
    
def test_should_return_message_money_not_less_than_total_price_when_pay_amount_less_than_total_price():
    mockstock = MockStockRpc(True,20)
    mockrpc = MockRPC(mockstock)
    Registry().rpc = mockrpc
    data = {
        "product_id": "test123",
        "pay_amount": 0,
        "pay_amount_detail": {100:1},
        "quantity": 20
        }
    response = client.post('/api/v1/create_order',json=data)
    assert response.json().get('message') == 'Money not less than total price' 
    assert response.status_code == 409
    
def test_should_return_message_not_enough_cash_for_change_money_when_pay_amount_more_than_cash_in_vending_machine():
    mockstock = MockStockRpc(True,20)
    mockvending = MockVendingMachineRpc(False,0,{})
    mockrpc = MockRPC(mockstock,mockvending)
    Registry().rpc = mockrpc
    data = {
        "product_id": "test123",
        "pay_amount": 200,
        "pay_amount_detail": {100:1},
        "quantity": 2
        }
    response = client.post('/api/v1/create_order',json=data)
    assert response.json().get('message') == 'Not enough cash for change money' 
    assert response.status_code == 409
    
def test_should_return_message_can_not_purchase_this_product_when_purchase_status_is_False():
    mockstock = MockStockRpc(True,20,False)
    mockvending = MockVendingMachineRpc(True,0,{})
    mockrpc = MockRPC(mockstock,mockvending)
    Registry().rpc = mockrpc
    data = {
        "product_id": "test123",
        "pay_amount": 20,
        "pay_amount_detail": {100:1},
        "quantity": 1
        }
    response = client.post('/api/v1/create_order',json=data)
    assert response.json().get('message') == 'Can not purchase this product' 
    assert response.status_code == 406
    
def test_should_return_message_success_and_chage_detail_with_status_200_when_product_is_already_and_pay_amount_is_more_or_equal_total_price_and_vending_machine_have_cash_to_change():
    mockstock = MockStockRpc(True,20,True)
    mockvending = MockVendingMachineRpc(True,0,{20:4})
    mockrpc = MockRPC(mockstock,mockvending)
    Registry().rpc = mockrpc
    Registry().transaction = InmemoryDB()
    data = {
        "product_id": "test123",
        "pay_amount": 100,
        "pay_amount_detail": {100:1},
        "quantity": 1
        }
    response = client.post('/api/v1/create_order',json=data)
    assert response.json().get('message') == 'success' 
    assert response.json().get('change_detail') == {'20':4}
    assert response.status_code == 200