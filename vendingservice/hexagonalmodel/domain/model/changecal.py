

def get_result(change,cashList):
    changeDetail = {}
    for cash,quantity in cashList:
        if change >= cash:
            changequantity = change // cash 
            if changequantity > quantity:
                changequantity = quantity
            changeDetail[cash] = changequantity
            change -= cash * changequantity
            
            if change == 0:
                break
    if change != 0:
        return False,{}
    return True,changeDetail