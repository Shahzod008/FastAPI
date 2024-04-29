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

## Использование напряму

1. Запустите сервер FastAPI:

    ```bash
    uvicorn main:app --reload
    ```

2. Откройте веб-браузер и перейдите по адресу http://127.0.0.1:8000/, для получения новостей.

## Использование через Docker
1. Создайте Docker контейнер с помощью команды
    ```bach
   docker build -t my-python-app .
   ```
2. Запустите контейнер с помощью команды
    ```bach
   docker run -d -p 8000:8000 my-python-app
    ```
3. Откройте веб-браузер и перейдите по адресу http://127.0.0.1:8000/, для получения новостей
4. 
## Эндпоинты

- Получить все Forex новости. http://127.0.0.1:8000/
- Параметры фильтрации:
     - `currency`: Фильтровать новостей по валюте. Пример http://127.0.0.1:8000/?currency=USD или http://127.0.0.1:8000/?currency=USD-EUR 
     - `importance`: Фильтровать новостей по уровню важности. Пример: http://127.0.0.1:8000/?importance=0 или http://127.0.0.1:8000/?importance=0-1
     - `currency-importance`: Фильтровать новостей по валюте и по уроню важности. Пример http://127.0.0.1:8000/?currency=USD-EUR&importance=2-3


## Автор
[Shahzod](https://github.com/Shahzod008)
