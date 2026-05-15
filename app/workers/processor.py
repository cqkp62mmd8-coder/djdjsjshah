import asyncio
from core.queue import queue_manager
from services.publisher import publish_message
from core.logger import log

async def worker_loop(worker_id: int):

    log.info(f"Worker-{worker_id} started")

    while True:
        item = await queue_manager.pop()

        if not item:
            continue

        try:
            await publish_message(item)

        except Exception as e:
            log.error(f"Worker-{worker_id} error: {e}")

        await asyncio.sleep(0.1)
