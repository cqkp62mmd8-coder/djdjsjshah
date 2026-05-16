from core.logger import log

class TelegramService:

    def __init__(self, client, channel):

        self.client = client

        self.channel = channel

    async def send(

        self,

        text,

        media=None,

        buttons=None

    ):

        try:

            msg = await self.client.send_message(

                self.channel,

                text,

                file=media,

                parse_mode="html",

                buttons=buttons

            )

            return msg

        except Exception as e:

            log.error(

                f"Telegram send failed: {e}"

            )

            return None
