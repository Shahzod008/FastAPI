import httpx
from fastapi import FastAPI, Query
from datetime import datetime
from bs4 import BeautifulSoup
from typing import Optional
import uvicorn

app = FastAPI()

FOREX_CALENDAR_URL = "https://www.forexfactory.com/calendar"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}


async def get_importance(row):
    if row.find(class_='icon icon--ff-impact-red'):
        return "Red"
    elif row.find(class_='icon icon--ff-impact-yel'):
        return "Yellow"
    elif row.find(class_="icon icon--ff-impact-ora"):
        return "Orange"
    elif row.find(class_="icon icon--ff-impact-gra"):
        return "Grey"


async def get_news_list():
    async with httpx.AsyncClient() as client:
        response = await client.get(FOREX_CALENDAR_URL, headers=HEADERS)
        soup = BeautifulSoup(response.content, features='html.parser')
        news_rows = soup.find_all(class_='calendar__row')
        result = []
        prev_date_time = None
        prev_date = None

        if news_rows:
            for row in news_rows:
                title_element = row.find(class_='calendar__event-title')
                title = title_element.get_text(strip=True) if title_element else None
                if not title:
                    continue

                date_time_element = row.find(class_='calendar__cell calendar__time')
                date_time_text = date_time_element.get_text(strip=True) if date_time_element else None
                if not date_time_text and prev_date_time:
                    date_time_text = prev_date_time

                prev_date_time = date_time_text

                date_element = row.find(class_='calendar__cell calendar__date')
                date_text = date_element.get_text(strip=True) if date_element else None
                if not date_text and prev_date:
                    date_text = prev_date

                prev_date = date_text

                currency_element = row.find(class_='calendar__cell calendar__currency')
                valuta = currency_element.get_text(strip=True) if currency_element else None

                importance = await get_importance(row)
                # cur = datetime.now().day
                #
                # numbers = [int(num) for num in date_text if num.isdigit()]
                # if numbers and int(''.join(map(str, numbers))) == cur:
                result.append({
                            'Заголовок': title,
                            'Время': date_time_text,
                            'Дата': date_text,
                            'Важность': importance,
                            'Валюта': valuta,
                        })

            return result


@app.get("/")
async def get_news(currency: Optional[str] = Query(None),
                   importance: Optional[str] = Query(None)):

    all_news = await get_news_list()

    if currency:
        currencies = currency.split('-')
        all_news = [news
                    for news in all_news
                    if any(c.lower() in news['Валюта'].lower()
                           for c in currencies)]

    if importance:
        importance_list = importance.split('-')
        importance_levels = ["Red",
                             "Orange",
                             "Yellow",
                             "Grey"]

        selected_levels = [
            importance_levels[int(idx)]
            for idx in importance_list]

        all_news = [news
                    for news in all_news
                    if news['Важность'] in selected_levels]

    return all_news


if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)
