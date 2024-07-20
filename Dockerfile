# Используем официальный образ Python
FROM python:3.8

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем requirements.txt и устанавливаем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем содержимое текущей директории в рабочую директорию контейнера
COPY . .

# Запускаем Uvicorn
# CMD ["uvicorn", "app.main_basic:app", "--host", "0.0.0.0", "--port", "8000"]
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
