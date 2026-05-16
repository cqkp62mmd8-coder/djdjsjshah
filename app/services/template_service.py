def render_template(item):

    product = item["product"]

    score = item["score"]

    discount = item["discount"]

    store = item["store"]

    category = item["category"]

    prices = item.get("prices", [])

    text = []

    text.append(

        f"🔥 <b>%{discount} İNDİRİM</b>"

    )

    text.append(

        f"📊 Skor: <b>{score}/100</b>"

    )

    text.append("")

    text.append(

        f"📌 <b>{product}</b>"

    )

    text.append(

        f"🏪 {store}"

    )

    text.append(

        f"📂 {category}"

    )

    if len(prices) >= 2:

        text.append("")

        text.append(

            f"💰 {prices[-1]} TL"

        )

    text.append("")

    text.append("#Fırsat #İndirim")

    return "\n".join(text)
