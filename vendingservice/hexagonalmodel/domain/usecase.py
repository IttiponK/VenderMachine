from .registry import Registry
from .model import changecal

def get_changeStatus_and_changeDetail(pay_amount,totalprice):
    repo = Registry()
    change = pay_amount - totalprice
    cashList = repo.cashbag.get_all_cash()
    changeStatus,changeDetail = changecal.get_result(change,cashList)
    return changeStatus,change,changeDetail

def update_cash(changeObjupdate):
    repo = Registry()
    repo.cashbag.update_from_dict(changeObjupdate)