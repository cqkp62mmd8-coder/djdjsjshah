from core.config import settings
from core.logger import log
from services.parser_service import extract_discount, extract_links, extract_price
from services.duplicate_service import is_duplicate, mark_seen
from services.scoring_service import quality_score

async def handle_message(text: str):
    text = text or ""

    if is_duplicate(text):
        return None

    discount = extract_discount(text)
    links = extract_links(text)
    prices = extract_price(text)

    if discount < settings.MIN_INDIRIM:
        return None

    score = quality_score(
        discount=discount,
        has_link=len(links) > 0,
        has_price=len(prices) > 0
    )

    if score < settings.MIN_KALITE:
        log.warn(f"Low quality skipped: {score}")
        return None

    mark_seen(text)

    return {
        "text": text,
        "discount": discount,
        "links": links,
        "score": score
    }