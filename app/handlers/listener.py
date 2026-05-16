from handlers.message_handler import handle_message

from core.queue import queue_manager

from core.logger import log

async def on_telegram_message(event):

    result = await handle_message(

        event.message.text or ""

    )

    if not result:

        return

    await queue_manager.push({

        **result,

        "media": event.message.media

    })

    log.info(

        f"Queued | {result['store']} | score={result['score']}"

    )

