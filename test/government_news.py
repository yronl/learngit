#!/usr/bin/env python
# coding=utf-8

import requests
from bs4 import BeautifulSoup
import pymysql

print('连接到mysql服务器...')
db = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', db='news', charset='utf8')
print('连接上了!')
cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS GOVERNMENT")
sql = """CREATE TABLE GOVERNMENT (
        title CHAR(100) NOT NULL,
        href CHAR(100),
        time CHAR(50))"""

cursor.execute(sql)

# def get_news_article(news):
#     newsArticle = []
#     for p in news:
#         newsArticle.append(p.text.strip())
#     return newsArticle

def get_html(url):
    html = requests.get(url)
    html.encoding = 'utf-8'
    return html.text

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36"}
url = "http://www.gov.cn/zhengce/zuixin.htm"
r = requests.get(url, headers=headers)
if r.status_code == 200:
    soup = BeautifulSoup(r.content.decode('utf-8', 'ignore'), 'lxml')
    new_content = soup.find('div', class_='list').find_all("li")



    for item in new_content:
        news_title = item.find('a').get_text()
        news_href = item.find("a").get("href")
        if news_href.startswith("/zhengce"):
            news_href = "http://www.gov.cn" + news_href
        news_data = item.find('span').get_text().strip()
        # news_html = get_html(news_href)
        # news_soup = BeautifulSoup(news_html, "html.parser")
        # news = news_soup.find(id="UCAP-CONTENT").find_all("p")
        # article = get_news_article(news)

        insert_news = ("INSERT INTO GOVERNMENT(title,href,time)" "VALUES(%s,%s,%s)")
        new_info = (news_title, news_href, news_data,)
        cursor.execute(insert_news, new_info)
        db.commit()


print('爬取数据并插入mysql数据库完成...')