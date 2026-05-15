import json
from core.redis import redis_client, QUEUE_KEY

class RedisQueue:

    async def push(self, item: dict):
        await redis_client.rpush(QUEUE_KEY, json.dumps(item))

    async def pop(self):
        data = await redis_client.blpop(QUEUE_KEY, timeout=0)
        if not data:
            return None
        return json.loads(data[1])

queue_manager = RedisQueue()
