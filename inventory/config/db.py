from redis_om import get_redis_connection
from .dot_env import HOST, PORT, PASSWORD

redis = get_redis_connection(
    host=HOST,
    port=PORT,
    password=PASSWORD,
    decode_responses=True
)