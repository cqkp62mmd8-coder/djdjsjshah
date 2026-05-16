STORES = {

    "amazon": "Amazon TR",

    "trendyol": "Trendyol",

    "hepsiburada": "Hepsiburada",

    "n11": "N11"

}

def detect_store(text):

    text = (text or "").lower()

    for key, val in STORES.items():

        if key in text:

            return val

    return "E-Ticaret"
