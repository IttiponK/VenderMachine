from fastapi import APIRouter 
from ..hexagonalmodel.domain import usecase

router = APIRouter() 

@router.get('/')
async def index():
    usecase.product_is_already('test123',2)
    return {'message':"Hello Stock service"}

@router.get('/api/v1/allproduct')
async def allproduct():
    products = usecase.get_all_products()
    return {'data':products}