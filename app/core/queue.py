import json

from core.redis import redis_client

QUEUE_KEY = "firsat_queue"

FAILED_QUEUE = "failed_queue"

class RedisQueue:

    async def push(self, item):

        await redis_client.rpush(QUEUE_KEY, json.dumps(item))

    async def pop(self):

        data = await redis_client.blpop(QUEUE_KEY, timeout=0)

        if not data:

            return None

        return json.loads(data[1])

    async def fail(self, item):

        await redis_client.rpush(FAILED_QUEUE, json.dumps(item))

queue_manager = RedisQueue()

