# Используем официальный образ Python
FROM python:3.11-slim

# Устанавливаем зависимости системы
RUN apt-get update && apt-get install -y build-essential

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл зависимостей
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все содержимое проекта в контейнер
COPY . .

# Открываем порт 8000 для приложения
EXPOSE 8000

# Определяем команду для запуска приложения
CMD alembic upgrade head && gunicorn main:app --workers 2 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000
