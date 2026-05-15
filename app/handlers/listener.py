from core.queue import queue_manager
from handlers.message_handler import handle_message
from core.logger import log

async def on_telegram_message(event):

    result = await handle_message(event.message.text)

    if not result:
        return

    await queue_manager.push({
        "text": result["text"],
        "discount": result["discount"],
        "score": result["score"],
        "links": result["links"],
        "media": event.message.media,
        "chat": getattr(event.chat, "username", "unknown")
    })

    log.info(f"Queued: score={result['score']}")
