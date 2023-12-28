from models.order import Order
from fastapi import  Request
from schemas.order import order_schema
from config.dot_env import INVENTORY_API
import time, requests

def order_completed(order: Order, product_id: str, stock: int):
    try:
        time.sleep(5)
        order.status = 'completed'
        order.save()
        new_stock = stock - order.quantity
        new_product = requests.put(INVENTORY_API + 'products/' + product_id, json={'stock': new_stock}).json()
        print(new_product)
    except:
        order.status = 'failed'
        order.save()
    