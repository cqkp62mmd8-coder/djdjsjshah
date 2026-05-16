CATEGORIES = {

    "elektronik": [

        "iphone",

        "samsung",

        "laptop",

        "tablet",

        "kulaklık",

        "monitor"

    ],

    "giyim": [

        "nike",

        "adidas",

        "ayakkabı",

        "mont"

    ],

    "market": [

        "kahve",

        "çikolata",

        "gıda"

    ]

}

def detect_category(text):

    text = (text or "").lower()

    for category, keywords in CATEGORIES.items():

        for kw in keywords:

            if kw in text:

                return category

    return "genel"
