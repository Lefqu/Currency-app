from sqlalchemy import create_engine
from app.models import Base
from app.database import DATABASE_URL

# Используем синхронный движок для создания схемы
sync_engine = create_engine(DATABASE_URL.replace("sqlite+aiosqlite", "sqlite"), echo=True)

# Создаем все таблицы
Base.metadata.create_all(bind=sync_engine)
