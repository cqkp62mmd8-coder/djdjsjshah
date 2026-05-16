import asyncio
from telethon import TelegramClient, events

from core.config import settings
from handlers.listener import on_telegram_message
from workers.processor import ProcessorWorker
from services.publisher import Publisher
from services.telegram_service import TelegramService

client = TelegramClient("session", settings.API_ID, settings.API_HASH)

async def main():

    await client.start()

    tg_service = TelegramService(client, settings.CHANNEL_ID)
    publisher = Publisher(tg_service)
    worker = ProcessorWorker(publisher)

    # Listener
    @client.on(events.NewMessage(chats=[]))
    async def handler(event):
        await on_telegram_message(event)

    # Workers
    for i in range(4):
        asyncio.create_task(worker.run(i))

    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())
