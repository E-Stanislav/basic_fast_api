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

# Определим маршрут для получения статьи по ID
@app.get("/mode/{mode_id}")
async def get_mode(mode_id: int):
    return {
        "mode": mode_id
    }