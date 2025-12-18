# My Application

Простое веб-приложение на FastAPI с автоматизированным CI/CD пайплайном на GitHub Actions.

## Функциональность
- Проверка состояния сервиса
- Сложение двух чисел через HTTP API

## CI/CD
Pipeline включает:
- автоматический запуск unit и интеграционных тестов
- сборку Docker-образа после успешных тестов
- публикацию образа в Docker Hub

```
## Запуск локально
docker build -t my-application .
docker run -d -p 8000:8000 my-application
```


