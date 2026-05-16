def calculate_quality_score(

    discount,

    has_link,

    has_price,

    has_product

):

    score = 0

    if discount >= 70:

        score += 40

    elif discount >= 50:

        score += 30

    elif discount >= 30:

        score += 20

    if has_link:

        score += 20

    if has_price:

        score += 20

    if has_product:

        score += 20

    return score
