from pydantic import BaseModel

class CurrencyBase(BaseModel):
    name: str
    buy_price: float
    sell_price: float
    current_rate: float

class CurrencyCreate(CurrencyBase):
    pass

class Currency(CurrencyBase):
    id: int

    class Config:
        orm_mode = True
