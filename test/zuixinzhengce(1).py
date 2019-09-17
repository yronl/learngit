# coding=utf-8
from bs4 import BeautifulSoup
import requests
import os
import csv
import time


def get_html(url):
    html = requests.get(url)
    html.encoding = 'utf-8'
    return html.text


def get_news_article(news):
    newsArticle = []
    for p in news:
        newsArticle.append(p.text.strip())
    return newsArticle


base_url = "http://www.gov.cn/zhengce/zuixin.htm"

path = os.getcwd() + "最新政策_data.csv"
csvfile = open(path, "a+", encoding='utf-8', newline='')
writer = csv.writer(csvfile)
writer.writerow(("标题", "时间", "链接", "内容"))

page_text = get_html(base_url)

root_soup = BeautifulSoup(page_text, "html.parser")

list_items = root_soup.find('div', class_='list list_1 list_2').find_all('li')
print(list_items)

for item in list_items:
    news_title = item.find('a').get_text()
    news_data = item.find('span').get_text().strip()
    news_url = item.find('a').get("href").strip()
    if news_url.startswith("/zhengce"):
        news_url = "http://www.gov.cn" + news_url

    news_html = get_html(news_url)
    news_soup = BeautifulSoup(news_html, "html.parser")
    news = news_soup.find(id="UCAP-CONTENT") .find_all("p")
    # print( news is None )
    article = get_news_article(news)
    print(news_title + ":::" + news_data)
    time.sleep(2)
    writer.writerow((news_title, news_data, news_url, article))

# writer.close()
print(path)
