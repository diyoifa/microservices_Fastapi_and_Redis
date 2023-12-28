from fastapi import APIRouter, status, HTTPException, Request
from fastapi.background import BackgroundTasks
from schemas.order import order_schema, order_schema_list
from models.order import Order
from utils.calculate_fee import fee
from utils.calculate_total import total
from utils.order_completed import order_completed
from config.dot_env import INVENTORY_API
import requests

router = APIRouter(
    prefix='/orders',
    tags=['orders']
)

@router.get('/')
async def all():
    try:
        return order_schema_list(Order.all_pks())
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Internal Server Error')

@router.get('/{id}', status_code=status.HTTP_200_OK)
async def get(id: str):
    try:
        return order_schema(Order.get(id))
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Order not found')

@router.post('/')
async def create(request: Request, background_tasks: BackgroundTasks):
    try:
        body = await request.json() #id quantity
        # print(body)
        product = requests.get(INVENTORY_API + 'products/' + body['product_id']).json()
        fee_for_product =  fee(float(body['quantity']))
        total_payment =  total(float(product['price']), fee_for_product, float(body['quantity']))

        new_order = Order(
            product_id=body['product_id'],
            price=product['price'],
            fee=fee_for_product,
            total=total_payment,
            quantity=body['quantity'],
            status='pending'
        )
        new_order.save()
        background_tasks.add_task(order_completed, new_order, body['product_id'], product['stock'])

        #hace una request para modificar el producto y restarle la cantidad
        return order_schema(new_order)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f'{str(e)}')

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete(id: str):
    try:
        # Order.delete_many({})
        # Order.save()
        Order.delete(id)
        return {"message": "Order deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f'{str(e)}')