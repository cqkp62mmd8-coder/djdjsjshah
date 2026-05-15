import asyncio

class QueueManager:
    def __init__(self, size=100):
        self.queue = asyncio.Queue(maxsize=size)

    async def push(self, item):
        if self.queue.full():
            await self.queue.get()  # backpressure strategy
        await self.queue.put(item)

    async def pop(self):
        return await self.queue.get()

queue_manager = QueueManager()