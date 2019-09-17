#__author__:YR
#__info__:None


import requests
from bs4 import BeautifulSoup

def main():
    url = "http://www.gov.cn/zhengce/zuixin.htm"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36"}
    response = requests.get(url, headers=headers)
    response.encoding = "utf8"

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, "lxml")
        content = soup.find('div', class_='list').find_all('li')


        for item in content:
            news_title = item.find('a').get_text()
            news_href = item.find("a").get("href")
            if news_href.startswith("/zhengce"):
                news_href = "http://www.gov.cn" + news_href
            news_data = item.find('span').get_text().strip()
            print(news_title + "->" + news_href+ "time->" +news_data)


if __name__ == "__main__":
    main()







