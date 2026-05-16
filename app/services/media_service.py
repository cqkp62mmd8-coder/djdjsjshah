from io import BytesIO

from PIL import Image

import os

LOGO_FILE = "logo.PNG"

async def process_image(client, media):

    if not media:

        return None

    try:

        raw = await client.download_media(

            media,

            bytes

        )

        if not raw:

            return None

        if not os.path.exists(LOGO_FILE):

            return BytesIO(raw)

        base = Image.open(

            BytesIO(raw)

        ).convert("RGBA")

        logo = Image.open(

            LOGO_FILE

        ).convert("RGBA")

        bw, bh = base.size

        target_w = int(bw * 0.22)

        ratio = target_w / logo.size[0]

        target_h = int(

            logo.size[1] * ratio

        )

        logo = logo.resize(

            (target_w, target_h)

        )

        x = bw - target_w - 15

        y = bh - target_h - 15

        base.paste(

            logo,

            (x, y),

            logo

        )

        output = BytesIO()

        base.convert("RGB").save(

            output,

            format="JPEG",

            quality=92

        )

        output.seek(0)

        output.name = "deal.jpg"

        return output

    except:

        return None
