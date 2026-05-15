from core.db import SessionLocal
from storage.models import Deal

def save_deal(item):
    db = SessionLocal()

    try:
        deal = Deal(
            discount=item["discount"],
            score=item["score"],
            store=item.get("store", "unknown"),
            category=item.get("category", "genel"),
            link=item["links"][0] if item.get("links") else None
        )

        db.add(deal)
        db.commit()
    except Exception as e:
        db.rollback()
    finally:
        db.close()
