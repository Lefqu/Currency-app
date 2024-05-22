from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app import crud, models, schemas
from app.database import async_engine, get_db
import uvicorn

# Убедитесь, что создаете таблицы в синхронном режиме, как было описано ранее.
# Создание таблиц необходимо выполнить отдельно через синхронный движок.

app = FastAPI()

@app.post("/currencies/", response_model=schemas.Currency)
async def create_currency(currency: schemas.CurrencyCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_currency(db, currency)

@app.get("/currencies/{currency_id}", response_model=schemas.Currency)
async def read_currency(currency_id: int, db: AsyncSession = Depends(get_db)):
    db_currency = await crud.get_currency(db, currency_id)
    if db_currency is None:
        raise HTTPException(status_code=404, detail="Currency not found")
    return db_currency

@app.get("/currencies/", response_model=list[schemas.Currency])
async def read_currencies(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    return await crud.get_currencies(db, skip=skip, limit=limit)

@app.put("/currencies/{currency_id}", response_model=schemas.Currency)
async def update_currency(currency_id: int, currency: schemas.CurrencyCreate, db: AsyncSession = Depends(get_db)):
    db_currency = await crud.update_currency(db, currency_id, currency)
    if db_currency is None:
        raise HTTPException(status_code=404, detail="Currency not found")
    return db_currency

@app.delete("/currencies/{currency_id}", response_model=dict)
async def delete_currency(currency_id: int, db: AsyncSession = Depends(get_db)):
    success = await crud.delete_currency(db, currency_id)
    if not success:
        raise HTTPException(status_code=404, detail="Currency not found")
    return {"message": "Currency deleted successfully"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
