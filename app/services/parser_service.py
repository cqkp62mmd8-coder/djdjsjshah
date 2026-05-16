import re

def extract_discount(text):

    if not text:

        return 0

    patterns = [

        r"(\d+)\s*%",

        r"%\s*(\d+)",

        r"indirim.*?(\d+)"

    ]

    values = []

    for pattern in patterns:

        matches = re.findall(pattern, text.lower())

        for m in matches:

            try:

                val = int(m)

                if 1 <= val <= 99:

                    values.append(val)

            except:

                pass

    return max(values) if values else 0

def extract_links(text):

    return re.findall(r'https?://[^\s]+', text or "")

def extract_prices(text):

    return re.findall(

        r'([\d.,]+)\s*(?:tl|₺)',

        text.lower()

    )

def extract_product_name(text):

    if not text:

        return None

    lines = text.split("\n")

    for line in lines:

        line = line.strip()

        if (

            len(line) > 10

            and "http" not in line

            and "%" not in line

            and "tl" not in line.lower()

        ):

            return line[:120]

    return None

