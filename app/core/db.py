from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

engine = create_engine("sqlite:///analytics.db")  # şimdilik sqlite (prod: postgres)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
