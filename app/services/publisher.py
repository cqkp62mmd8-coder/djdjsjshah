from core.logger import log
from core.config import settings

async def publish_message(item):

    text = item["text"]
    score = item["score"]
    links = item.get("links", [])

    final_text = f"🔥 Fırsat Skoru: {score}/10\n\n{text}"

    # burada TELEGRAM SEND BAĞLANACAK
    # (client inject edeceğiz main'de)

    log.info(f"Published score={score}")

    return final_text
