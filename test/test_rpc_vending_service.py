from vendingservice.hexagonalmodel.domain import usecase 
from vendingservice.hexagonalmodel.domain.registry import Registry
from vendingservice.hexagonalmodel.adapter.inmemory import InmemoryDB
mockcashbag =  [[1000,1],[500,3],[100,10],[50,4],[20,10],[10,10],[5,20],[1,100]]

Registry().cashbag = InmemoryDB(mockcashbag)
def test_should_return_changeStatus_equal_True_and_changeDetail_when_cash_bag_is_more_or_equal_change():
    pay_amount = 500
    totalprice = 30
    changeStatus,change,changeDetail = usecase.get_changeStatus_and_changeDetail(pay_amount,totalprice)
    assert changeStatus == True 
    assert change == 470
    assert changeDetail == {100:4,50:1,20:1}
    
def test_should_return_changeStatus_equal_False_when_cashbag_not_enough_to_change():
    pay_amount = 5000
    totalprice = 30
    changeStatus,change,changeDetail = usecase.get_changeStatus_and_changeDetail(pay_amount,totalprice)
    assert changeStatus == False

def test_should_return_changeDetail_body_is_500_equal_1_100_equal_4_50_equal_1_20_equal_1_10_equal_1_5_equal_1_1_equal_3_when_pay_amount_1000_and_totalprice_12():
    pay_amount = 1000
    totalprice = 12
    changeStatus,change,changeDetail = usecase.get_changeStatus_and_changeDetail(pay_amount,totalprice)
    assert changeStatus == True 
    assert change == 988
    assert changeDetail == {500:1,100:4,50:1,20:1,10:1,5:1,1:3}