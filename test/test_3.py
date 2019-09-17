#__author__:YR
#__info__:None


import requests
from requests.exceptions import RequestException
from multiprocessing import Pool
import re
import json
import openpyxl


def get_one_page(url, headers):
    try:
        response = requests.get(url, headers=headers)
        response.encoding = "utf8"
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

def parse_one_page(html):

    pattern = re.compile(r'<a href=.*?>(.*?)</a>')
    # pattern = re.compile(r'<span.*?>.</span>')


    items = re.findall(pattern, html)
    for item in items:
        print(item)



def main():
    url = "http://www.gov.cn/zhengce/zuixin.htm"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36"}
    html = get_one_page(url, headers)
    parse_one_page(html)



if __name__ == "__main__":
   main()

