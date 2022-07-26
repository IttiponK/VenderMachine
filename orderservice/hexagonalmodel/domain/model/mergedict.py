

def merge(changeDetail:dict,pay_amount_detail:dict):
    cashObjupdate = changeDetail.copy()
    for key,value in pay_amount_detail.items():
        if changeDetail.get(key):
            cashObjupdate[int(key)] = changeDetail.get(key) - value 
        else:
            cashObjupdate[int(key)] = -value 
    return cashObjupdate