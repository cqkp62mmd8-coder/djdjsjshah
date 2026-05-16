import hashlib

seen_cache = {}

def generate_hash(text):

    normalized = (

        text.lower()

        .replace(" ", "")

        .strip()

    )

    return hashlib.md5(

        normalized.encode()

    ).hexdigest()

def is_duplicate(text):

    h = generate_hash(text)

    return h in seen_cache

def remember(text):

    h = generate_hash(text)

    seen_cache[h] = True
