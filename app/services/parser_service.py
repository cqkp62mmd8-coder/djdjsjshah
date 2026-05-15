import re

def extract_discount(text: str):
    if not text:
        return 0

    matches = re.findall(r"(\d+)\s*%", text.lower())
    values = [int(m) for m in matches if 1 <= int(m) <= 99]

    return max(values) if values else 0


def extract_links(text: str):
    return re.findall(r'https?://[^\s]+', text or "")


def extract_price(text: str):
    matches = re.findall(r"([\d.,]+)\s*(?:tl|₺)", text.lower())
    return matches