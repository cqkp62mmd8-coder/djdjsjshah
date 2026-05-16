from core.logger import log

class TelegramService:
    def __init__(self, client, channel_id):
        self.client = client
        self.channel_id = channel_id

    async def send(self, text, media=None, buttons=None, silent=False):

        try:
            msg = await self.client.send_message(
                self.channel_id,
                text,
                file=media,
                parse_mode="html",
                buttons=buttons,
                silent=silent
            )
            return msg

        except Exception as e:
            log.error(f"Telegram send error: {e}")
            return None
