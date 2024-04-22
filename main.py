from fastapi import FastAPI, Query
import requests
from bs4 import BeautifulSoup
from typing import Optional

app = FastAPI()

FOREX_CALENDAR_URL = "https://www.forexfactory.com/calendar"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

response = requests.get(FOREX_CALENDAR_URL, headers=HEADERS)
soup = BeautifulSoup(response.content, 'html.parser')
news_rows = soup.find_all(class_='calendar__row')
news_list = []


def get_importance(row):
    if row.find(class_='icon icon--ff-impact-red'):
        return "Red"
    elif row.find(class_='icon icon--ff-impact-yel'):
        return "Yellow"
    elif row.find(class_="icon icon--ff-impact-ora"):
        return "Orange"
    elif row.find(class_="icon icon--ff-impact-gra"):
        return "Grey"


def get_news_list():
    result = []
    prev_date_time = None
    if news_rows:
        for row in news_rows:
            title_element = row.find(class_='calendar__event-title')
            title = title_element.get_text(strip=True) \
                if title_element else None
            if not title:
                continue

            date_time_element = row.find(class_='calendar__cell calendar__time')
            date_time_text = date_time_element.get_text(strip=True) \
                if date_time_element else ""
            if not date_time_text and prev_date_time:
                date_time_text = prev_date_time

            currency_element = row.find(class_='calendar__cell calendar__currency')
            valuta = currency_element.get_text(strip=True) \
                if currency_element else "No currency"

            importance = get_importance(row)

            result.append({
                'title': title,
                'date_time': date_time_text,
                'importance': importance,
                'valuta': valuta,
            })
            prev_date_time = date_time_text
    return result


@app.get("/")
def get_news(currency: Optional[str] = Query(None),
             importance: Optional[str] = Query(None)):
    all_news = get_news_list()

    if currency:
        currencies = currency.split('-')
        all_news = [news
                    for news in all_news
                    if any(c.lower() in news['valuta'].lower()
                           for c in currencies)]

    if importance:
        importance_list = importance.split('-')
        importance_levels = ["Red", "Orange", "Yellow", "Grey"]
        selected_levels = [importance_levels[int(idx)] for idx in importance_list]
        all_news = [news
                    for news in all_news
                    if news['importance'] in selected_levels]

    return all_news
