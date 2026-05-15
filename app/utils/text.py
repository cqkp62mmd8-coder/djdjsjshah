import re
import unicodedata

def clean_text(text: str):
    if not text:
        return ""
    return text.strip()

def remove_emojis(text: str):
    return "".join(
        c for c in text
        if unicodedata.category(c) not in ("So", "Sk", "Sm")
    )

def normalize(text: str):
    text = clean_text(text)
    text = remove_emojis(text)
    text = re.sub(r"\s+", " ", text)
    return text.lower()