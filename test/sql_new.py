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
        time CHAR(50) )"""

cursor.execute(sql)

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36"}

url = "http://www.gov.cn/zhengce/zuixin.htm"

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content.decode('utf-8', 'ignore'), 'lxml')
new_content = soup.find('div', class_='list').find_all("li")  # 获取全部tr标签成为一个列表
for item in new_content:              # 遍历列表里所有的tr标签单项
    news_title = item.find('a').get_text() # 获取每个tr标签里的属性style
    news_href = item.find("a").get("href") # 将每个tr标签下的td标签获取为列表
    if news_href.startswith("/zhengce"):
        news_href = "http://www.gov.cn" + news_href
    news_data = item.find('span').get_text().strip()

    # print u'颜色: ' + name + u'颜色值: '+ hex + u'背景色样式: ' + style
    # print 'color: ' + name + '\tvalue: '+ hex + '\tstyle: ' + style
    insert_news = ("INSERT INTO GOVERNMENT(title,href,time)" "VALUES(%s,%s,%s)")
    new_info = (news_title, news_href, news_data)
    cursor.execute(insert_news, new_info)
    db.commit()
    # print '******完成此条插入!'

print('爬取数据并插入mysql数据库完成...')