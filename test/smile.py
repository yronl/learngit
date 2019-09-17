#__author__:YR
#__info__:None

import requests
from lxml import etree
import pymysql

print("在慢慢连接到mysql...")
db = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', db='news', charset='utf8')
print("连上了。。。")
cursor = db.cursor()
cursor.execute("drop table if exists smile")
sql = """create table smile(
          con varchar(300))"""
cursor.execute(sql)

def get_html(url, headers):
    html = requests.get(url, headers=headers)
    html.encoding = "utf-8"
    return html.text

def main():
    url = "https://www.qiushibaike.com/"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36"}
    r = get_html(url, headers)
    soup = etree.HTML(r)
    content = soup.xpath('//div[@class="content"]/span/text()')
    num = range(0, 20)

    for a in content:
        con = a.strip()


        jxw_con = ("insert into smile(con)""values (%s)")
        jxw_info = (con)
        cursor.execute(jxw_con, jxw_info)
        db.commit()

if __name__ == "__main__":
    main()