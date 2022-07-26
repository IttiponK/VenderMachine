from fastapi import APIRouter,Response,status
from . import requestmodel
from ..hexagonalmodel.domain import usecase
from ..hexagonalmodel.domain.base.exception import (
    CashNotEnough,
    PayAmountNotLessthantotalprice,
    ProductIsnotAlready,
    PurchaseNotsuccess,
)
router = APIRouter()


@router.post('/api/v1/create_order',status_code=200)
async def create_order(order:requestmodel.Order,response:Response):
    try:
        message,change_detail = usecase.create_order(order)
        return {'message':message,'change_detail':change_detail}
    except ProductIsnotAlready:
        response.status_code = status.HTTP_406_NOT_ACCEPTABLE
        return {'message':'Product is not already'}
    except PayAmountNotLessthantotalprice:
        response.status_code = status.HTTP_409_CONFLICT
        return {'message':'Money not less than total price'}
    except CashNotEnough:
        response.status_code = status.HTTP_409_CONFLICT
        return {'message':'Not enough cash for change money'}
    except PurchaseNotsuccess:
        response.status_code = status.HTTP_406_NOT_ACCEPTABLE
        return {'message':'Can not purchase this product' }