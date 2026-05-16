import re

import unicodedata

def clean_text(text):

    if not text:

        return ""

    return text.strip()

def remove_emojis(text):

    return "".join(

        c for c in text

        if unicodedata.category(c) not in ("So", "Sk", "Sm")

    )

def normalize(text):

    text = clean_text(text)

    text = remove_emojis(text)

    text = re.sub(r"\s+", " ", text)

    return text.lower()
