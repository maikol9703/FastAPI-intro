from fastapi import APIRouter

router=APIRouter()

@router.get("/products/")
async def products():
    return ["banana","manzana","iphone"]