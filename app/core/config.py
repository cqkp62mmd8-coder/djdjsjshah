import os

class Settings:
    API_ID = int(os.getenv("API_ID", "0"))
    API_HASH = os.getenv("API_HASH", "")
    SESSION_STRING = os.getenv("SESSION_STRING", "")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "")
    CHANNEL_ID = os.getenv("CHANNEL_ID", "")
    ADMIN_ID = os.getenv("ADMIN_ID", "")

    MIN_INDIRIM = int(os.getenv("MIN_INDIRIM", "50"))
    MIN_KALITE = int(os.getenv("MIN_KALITE", "15"))
    KUYRUK_BEKLEME = int(os.getenv("KUYRUK_BEKLEME", "180"))

settings = Settings()