# Используем официальный образ Python
FROM python:3.9

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем requirements.txt и устанавливаем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Установка Redis
RUN apt-get update && apt-get install -y redis-server

# Копируем содержимое текущей директории в рабочую директорию контейнера
COPY . .

# Запускаем Redis и Uvicorn
CMD ["sh", "-c", "redis-server --daemonize yes && uvicorn app.main_no:app --host 0.0.0.0 --port 8000"]
