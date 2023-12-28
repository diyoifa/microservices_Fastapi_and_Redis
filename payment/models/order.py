from pydantic import BaseModel
from redis_om import get_redis_connection, HashModel
from config.db import redis



class Order(HashModel):
    product_id: str
    price: float
    fee: float
    total: float
    quantity: int
    status: str

    class Meta:
        database = redis

class OrderModel(BaseModel):
    product_id: str
    price: float
    fee: int
    total: float
    quantity: int
    status: str




