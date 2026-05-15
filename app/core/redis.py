import redis.asyncio as redis
from core.config import settings

redis_client = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)

QUEUE_KEY = "firsat_queue"
