#__author__:YR
#__info__:None
#爬取猫眼电影TOP100

import requests
from requests.exceptions import RequestException
from multiprocessing import Pool
import re
import json
import openpyxl

def get_one_page(url, headers):
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                         + '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         + '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)

    items = re.findall(pattern, html)
    print(items)


    # for item in items:
    #     yield {
    #         "index": item[0],
    #         "image": item[1],
    #         "title": item[2],
    #         "actor": item[3].strip()[3:],
    #         "time": item[4].strip()[5:],
    #         "score": item[5]+item[6]
    #     }
# def write_to_file(content):
#     with open("result.txt", "a", encoding="utf-8")as f:
#         f.write(json.dumps(content, ensure_ascii=False) + "\n")
#         f.close()
#

def main():

    url = "http://maoyan.com/board/4"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36"}
    html = get_one_page(url, headers)
    parse_one_page(html)
    # for item in parse_one_page(html):
    #     print(item)
    #     write_to_file(item)
    # print(html)


if __name__ == "__main__":
   main()
    # for i in range(10):
    #     main(i*10)
    # pool = Pool()
    # pool.map(main, [i*10 for i in range(10)])

