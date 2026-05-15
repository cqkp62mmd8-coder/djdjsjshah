from core.db import Base
from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime

class Deal(Base):
    __tablename__ = "deals"

    id = Column(Integer, primary_key=True)
    discount = Column(Integer)
    score = Column(Float)
    store = Column(String)
    category = Column(String)
    link = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
