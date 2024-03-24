from datetime import datetime

import requests
from bs4 import BeautifulSoup

from webapp.model import db, News

def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        print("Сетевая ошибка")
        return False

def get_python_news():
    html = get_html("https://www.kino-teatr.ru/kino/news/")
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        all_news = soup.find("div", class_="grid_content wrap_cols_4 width_100").findAll("article")
        result_news = []
        for news in all_news:
            title = news.find('a')['title']
            url = 'https://www.kino-teatr.ru/' + news.find('a')['href']
            published = news.find('time')['datetime']
            img_icon = 'https://www.kino-teatr.ru/' + news.find('img')['src']
            try:
                published = datetime.strptime(published, "%Y-%m-%d %H:%M:%S")
            except(ValueError):
                published = datetime.now()
            save_news(title, url, published, img_icon)

def save_news(title, url, published, img_icon):
    news_exists = News.query.filter(News.url == url).count()
    if not news_exists:
        new_news = News(title=title, url=url, published=published, img_icon=img_icon)
        db.session.add(new_news)
        db.session.commit()