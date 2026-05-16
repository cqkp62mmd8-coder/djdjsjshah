from core.logger import log

class Publisher:

    def __init__(self, telegram_service):
        self.tg = telegram_service

    async def publish(self, item):

        text = item["text"]
        score = item["score"]
        links = item.get("links", [])
        media = item.get("media")

        final_text = f"🔥 <b>Fırsat Skoru: {score}/10</b>\n\n{text}"

        buttons = None
        if links:
            from telethon.tl.types import KeyboardButtonUrl, KeyboardButtonRow, ReplyInlineMarkup

            buttons = ReplyInlineMarkup(rows=[
                KeyboardButtonRow(buttons=[
                    KeyboardButtonUrl(text="🔗 Fırsata Git", url=links[0])
                ])
            ])

        msg = await self.tg.send(
            text=final_text,
            media=media,
            buttons=buttons,
            silent=False
        )

        if msg:
            log.info(f"Published OK | score={score}")

        return msg
