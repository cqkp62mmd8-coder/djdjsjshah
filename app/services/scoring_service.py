def quality_score(discount: int, has_link: bool, has_price: bool):
    score = 0

    if discount >= 50:
        score += 40
    elif discount >= 30:
        score += 25
    else:
        score += 10

    if has_link:
        score += 20

    if has_price:
        score += 20

    return score