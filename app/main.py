import asyncio
from telethon import TelegramClient, events

from core.config import settings
from handlers.listener import on_telegram_message
from workers.processor import worker_loop

client = TelegramClient("session", settings.API_ID, settings.API_HASH)

async def start_workers():
    for i in range(4):  # scalable concurrency layer
        asyncio.create_task(worker_loop(i))

async def main():
    await client.start()

    @client.on(events.NewMessage(chats=[]))
    async def handler(event):
        await on_telegram_message(event)

    await start_workers()

    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())
