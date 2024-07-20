# Простая реализация GET запросов через FastApi

# Запуск процесса через Dockerfile
## Сбилдить образ
```shell
docker build -t fastapi-app:latest .
```
## Запустить образ
```shell
docker run -p 8000:8000 -p 6379:6379 fastapi-app:latest
```

# Запуск процесса через docker-compose
```
docker-compose up -d
```