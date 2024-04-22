[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
# API Forex Новости

## Описание
**API Форекс Новости** - это API предоставляющий доступ к последним  [Forex](https://www.forexfactory.com) новостям с [Forex Factory](https://www.forexfactory.com). Он позволяет фильтровать новости по валютам и уровню важности.

## Технологии
  - [Python 3.11](https://www.python.org/downloads/release/python-3119)
  - [FastApi 0.110.2](https://fastapi.tiangolo.com/)
  - [Beautiful Soup 4.12](https://beautiful-soup-4.readthedocs.io/en/latest/)
  
## Установка

1. Склонируйте репозиторий:

    ```bash
    git clone https://github.com/Shahzod008/FastAPI.git
    ```

2. Установите необходимые зависимости:

    ```bash
    pip install -r requirements.txt
    ```

## Использование

1. Запустите сервер FastAPI:

    ```bash
    uvicorn main:app --reload
    ```

2. Откройте веб-браузер и перейдите по адресу `http://localhost:8000`, для получения новостей.

## Эндпоинты

- Получить все Forex новости. `http://localhost:8000/`
- Параметры фильтрации:
    - `currency`: Фильтровать новости по валюте. Например `https://localhost:8000/?currency=USD` или `https://localhost:8000/?currency=USD-EUR` 
    - `importance`: Фильтровать новости по уровню важности. Пример: `https://localhost:8000/?importance=0`

## Автор
[Shahzod](https://github.com/Shahzod008)
