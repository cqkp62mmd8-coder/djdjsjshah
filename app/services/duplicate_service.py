import hashlib

_seen = {}

def make_key(text: str):
    text = (text or "").lower().replace(" ", "")
    return hashlib.md5(text.encode()).hexdigest()


def is_duplicate(text: str):
    key = make_key(text)
    return key in _seen


def mark_seen(text: str):
    key = make_key(text)
    _seen[key] = True