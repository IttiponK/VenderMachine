from stockservice.rest.initapp import create_app 
from fastapi.testclient import TestClient
from stockservice.hexagonalmodel.domain.model.stock import Stock
from stockservice.hexagonalmodel.adapter.inmemory import InmemoryDB 
from stockservice.hexagonalmodel.domain.registry import Registry

client = TestClient(create_app(InmemoryDB(Stock)))
test_dependency = InmemoryDB(Stock)
    
    
def test_get_all_product_in_stock_response_dot_data_should_be_list():
    Registry().stock = test_dependency
    response = client.get('/api/v1/allproduct')
    assert type(response.json().get('data')) == list
    
def test_get_all_product_should_contain_product_detail_as_product_id_name_price_quantity():
    Registry().stock = test_dependency
    response = client.get('/api/v1/allproduct')
    data = response.json().get('data') 
    keycheck = data[0].get('product_id') and data[0].get('name') and data[0].get('price') and data[0].get('quantity')
    assert keycheck != None