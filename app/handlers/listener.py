from core.queue import queue_manager
from handlers.message_handler import handle_message

async def on_telegram_message(event):
    result = await handle_message(event.message.text)

    if not result:
        return

    await queue_manager.push({
        "text": result["text"],
        "score": result["score"],
        "links": result["links"],
        "discount": result["discount"],
        "media": event.message.media
    })