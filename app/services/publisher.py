from core.config import settings
from core.logger import log

async def publish_message(item):
    text = item["text"]
    score = item["score"]

    # burada ileride image processing + formatting + AI rewrite gelecek
    final_text = f"[{score}/10]\n\n{text}"

    # placeholder send (main client inject edilecek sonra)
    log.info(f"Publishing: score={score}")

    return final_text