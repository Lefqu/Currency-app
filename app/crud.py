from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Currency
from app.schemas import CurrencyCreate

async def get_currency(db: AsyncSession, currency_id: int):
    result = await db.execute(select(Currency).filter(Currency.id == currency_id))
    return result.scalars().first()

async def get_currencies(db: AsyncSession, skip: int = 0, limit: int = 100):
    result = await db.execute(select(Currency).offset(skip).limit(limit))
    return result.scalars().all()

async def create_currency(db: AsyncSession, currency: CurrencyCreate):
    db_currency = Currency(**currency.dict())
    db.add(db_currency)
    await db.commit()
    await db.refresh(db_currency)
    return db_currency

async def delete_currency(db: AsyncSession, currency_id: int):
    result = await db.execute(select(Currency).filter(Currency.id == currency_id))
    db_currency = result.scalars().first()
    if db_currency:
        await db.delete(db_currency)
        await db.commit()
        return True
    return False

async def update_currency(db: AsyncSession, currency_id: int, currency: CurrencyCreate):
    result = await db.execute(select(Currency).filter(Currency.id == currency_id))
    db_currency = result.scalars().first()
    if db_currency:
        for key, value in currency.dict().items():
            setattr(db_currency, key, value)
        await db.commit()
        await db.refresh(db_currency)
        return db_currency
    return None
