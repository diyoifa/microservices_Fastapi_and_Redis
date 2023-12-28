from pydantic import BaseModel
from redis_om import get_redis_connection, HashModel
from config.db import redis

# redis = get_redis_connection(
#     host="redis-16523.c274.us-east-1-3.ec2.cloud.redislabs.com",
#     port=16523,
#     password="sa54d6adjdfads4f465154dasd1asdasd",
#     decode_responses=True
# )

class Product(HashModel):
    name: str
    price: float
    stock: int

    class Meta:
        database = redis

class ProductModel(BaseModel):
    name: str
    price: float
    stock: int

