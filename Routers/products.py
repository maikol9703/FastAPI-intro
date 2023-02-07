from fastapi import APIRouter

router=APIRouter(prefix="/products",tags=["products"],responses={404:{"message":"page not found"}})

products_list=["banana","iphone","rice","ice cream"]

@router.get("/")
async def products():
    return products_list

@router.get("/{id}")
async def products(id:int):
    return products_list[id]