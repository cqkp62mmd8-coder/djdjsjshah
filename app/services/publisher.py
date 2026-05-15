from core.logger import log
from storage.analytics import save_deal

async def publish_message(item):

    text = item["text"]
    score = item["score"]

    final_text = f"🔥 [{score}/10]\n\n{text}"

    # analytics pipeline
    save_deal(item)

    log.info(f"PUBLISHED | score={score}")

    # burada Telegram send gelecek (inject edilecek)
    return final_text
