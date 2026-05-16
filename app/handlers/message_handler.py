from services.parser_service import (

    extract_discount,

    extract_links,

    extract_prices,

    extract_product_name

)

from services.category_service import detect_category

from services.store_service import detect_store

from services.scoring_service import calculate_quality_score

from services.duplicate_service import (

    is_duplicate,

    remember

)

from services.ai_service import ai_rewrite

from core.config import settings

async def handle_message(text):

    if not text:

        return None

    if is_duplicate(text):

        return None

    discount = extract_discount(text)

    if discount < settings.MIN_INDIRIM:

        return None

    links = extract_links(text)

    prices = extract_prices(text)

    product = extract_product_name(text)

    category = detect_category(text)

    store = detect_store(text)

    score = calculate_quality_score(

        discount=discount,

        has_link=len(links) > 0,

        has_price=len(prices) > 0,

        has_product=product is not None

    )

    if score < settings.MIN_KALITE:

        return None

    remember(text)

    rewritten = ai_rewrite(product, score)

    return {

        "text": text,

        "discount": discount,

        "links": links,

        "prices": prices,

        "product": rewritten,

        "category": category,

        "store": store,

        "score": score

    }
