import asyncio
from telethon import TelegramClient, events
from core.config import settings
from core.logger import log
from handlers.message_handler import handle_message

client = TelegramClient("session", settings.API_ID, settings.API_HASH)

@client.on(events.NewMessage(chats=[]))
async def on_message(event):
    result = await handle_message(event.message.text)

    if not result:
        return

    log.info(f"Accepted: score={result['score']}")
    await client.send_message(settings.CHANNEL_ID, result["text"])


async def main():
    await client.start()
    log.info("System started")
    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())