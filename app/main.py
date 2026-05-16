import asyncio

from telethon import (

    TelegramClient,

    events

)

from telethon.sessions import (

    StringSession

)

from core.config import settings

from handlers.listener import (

    on_telegram_message

)

from workers.processor import (

    ProcessorWorker

)

from services.telegram_service import (

    TelegramService

)

from services.publisher import (

    Publisher

)

from core.logger import log

SOURCE_CHANNELS = [

    "@amazonsicakfirsatlar",

    "@donanimhabersicakfirsatlar",

    "@firsatpaylasim"

]

client = TelegramClient(

    StringSession(settings.SESSION_STRING),

    settings.API_ID,

    settings.API_HASH

)

async def main():

    await client.start()

    log.info("Client connected")

    tg_service = TelegramService(

        client,

        settings.CHANNEL_ID

    )

    publisher = Publisher(

        tg_service,

        client

    )

    worker = ProcessorWorker(

        publisher

    )

    for i in range(4):

        asyncio.create_task(

            worker.run(i)

        )

    @client.on(

        events.NewMessage(

            chats=SOURCE_CHANNELS

        )

    )

    async def handler(event):

        await on_telegram_message(

            event

        )

    log.info("System online")

    await client.run_until_disconnected()

if __name__ == "__main__":

    asyncio.run(main())
