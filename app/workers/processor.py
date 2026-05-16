import asyncio
from core.queue import queue_manager
from core.logger import log

class ProcessorWorker:

    def __init__(self, publisher):
        self.publisher = publisher

    async def run(self, worker_id: int):

        log.info(f"Worker-{worker_id} started")

        while True:
            item = await queue_manager.pop()

            if not item:
                continue

            try:
                await self.publisher.publish(item)

            except Exception as e:
                log.error(f"Worker-{worker_id} failed: {e}")

            await asyncio.sleep(0.1)
