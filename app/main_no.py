from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
import random

# Определим модель статьи
class Article(BaseModel):
    id: int
    title: str
    long_title: str
    annotation: str
    author: str
    source: str

# Создадим экземпляр FastAPI
app = FastAPI()

def get_article_from_db(article_id: int):
    try:
        with sqlite3.connect('app/database.db') as db:
            cursor = db.cursor()
            cursor.execute("SELECT * FROM articles WHERE id = ?", (article_id,))
            article = cursor.fetchone()
            if not article:
                raise HTTPException(status_code=404, detail="Статья не найдена")
            return article
    except sqlite3.Error:
        raise HTTPException(status_code=500, detail="Ошибка базы данных")

def get_article(article_id: int):    
    article = get_article_from_db(article_id)
    return article

@app.get("/articles/{article_id}", response_model=Article)
async def read_article(article_id: int):
    article = get_article_from_db(article_id)
    return Article(
        id=article[0],
        title=article[1],
        long_title=article[2],
        annotation=article[3],
        author=article[4] if article[4] else "",
        source=article[5]
    )

@app.get("/random", response_model=Article)
async def read_random_article():
    article_id = random.randint(1, 5000)
    article = get_article_from_db(article_id)
    return Article(
        id=article[0],
        title=article[1],
        long_title=article[2],
        annotation=article[3],
        author=article[4] if article[4] else "",
        source=article[5]
    )
