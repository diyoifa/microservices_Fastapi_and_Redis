from fastapi import APIRouter, status, HTTPException, Request
from schemas.product import product_schema, product_schema_list
from models.product import Product, ProductModel

router = APIRouter(
    prefix='/products',
    tags=['products']
)

@router.get('/', status_code=status.HTTP_200_OK)
async def all():
    try:
        return product_schema_list(Product.all_pks())
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Internal Server Error')

@router.get('/{id}')
async def get(id: str):
    try:
        product = Product.get(id)
        return product_schema(product)
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Product not found')

@router.post('/', status_code=status.HTTP_201_CREATED)
async def create(product: ProductModel):
    try:
        product_db = Product(**product.__dict__)
        product_db.save()
        return product_schema(product_db)
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Internal Server Error')

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete(id: str):
    try:
        Product.delete(id)
        return {"message": "Product deleted successfully"}
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Product not found')

@router.put('/{id}', status_code=status.HTTP_200_OK)
async def update(id:str, request: Request):
    try:
        body = await request.json()
        product_db = Product.get(id)
        product_db.update(**body)
        product_db.save()
        return product_schema(product_db)
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Product not found')
