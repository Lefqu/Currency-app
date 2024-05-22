from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Currency(Base):
    __tablename__ = "currencies"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    buy_price = Column(Float)
    sell_price = Column(Float)
    current_rate = Column(Float)
