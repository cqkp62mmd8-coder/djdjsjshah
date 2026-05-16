from services.template_service import render_template

from services.media_service import process_image

from telethon.tl.types import (

    KeyboardButtonUrl,

    KeyboardButtonRow,

    ReplyInlineMarkup

)

from core.logger import log

class Publisher:

    def __init__(

        self,

        tg_service,

        client

    ):

        self.tg = tg_service

        self.client = client

    async def publish(self, item):

        final_text = render_template(item)

        media = await process_image(

            self.client,

            item.get("media")

        )

        buttons = None

        links = item.get("links", [])

        if links:

            buttons = ReplyInlineMarkup(

                rows=[

                    KeyboardButtonRow(

                        buttons=[

                            KeyboardButtonUrl(

                                text="🔗 Fırsata Git",

                                url=links[0]

                            )

                        ]

                    )

                ]

            )

        msg = await self.tg.send(

            text=final_text,

            media=media,

            buttons=buttons

        )

        if msg:

            log.info(

                f"PUBLISHED | {item['store']} | score={item['score']}"

            )

        return msg
