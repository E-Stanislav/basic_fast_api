from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import sqlite3
import redis

# Определим модель статьи
class Article(BaseModel):
    id: int
    title: str
    content: str

# Создадим экземпляр FastAPI
app = FastAPI()

# Подключаемся к Redis
# r = redis.Redis(host='127.0.0.1', port=6379, db=0)

# Подключимся к базе данных SQLite

# db = sqlite3.connect('app/test.db')
db = sqlite3.connect('app/test.db')
cursor = db.cursor()

# Определим маршрут для получения статьи по ID
@app.get("/articles/{article_id}")
async def get_article(article_id: int):
    # Попробуем найти статью в базе данных

    cursor.execute("SELECT * FROM articles WHERE id = ?", (article_id,))
    article = cursor.fetchone()

    # Если статья не найдена, вернем ошибку 404
    if not article:
        raise HTTPException(status_code=404, detail="Статья не найдена")

    # r.set(article_id, article)
    # Преобразуем результат из базы данных в модель Article
    return Article(id=article[0], title=article[1], content=article[2])


# Определим маршрут для получения статьи по ID
@app.get("/mode/{mode_id}")
async def get_mode(mode_id: int):
    return {
        "mode": mode_id
    }