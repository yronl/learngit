#__author__:YR
#__info__:None

import requests
from bs4 import BeautifulSoup
import re

from lxml import etree

# resp = requests.urlopen('http://wufazhuce.com/one/' + str(2161 + i))
def get_html(url, headers):
    html = requests.get(url, headers=headers)
    html.encoding = 'utf-8'
    return html.text

# f = open("f:/jitang.txt", "w", encoding="utf-8")
for i in range(0, 100):
    url = 'http://wufazhuce.com/one/' + str(2309 - i)
    headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Mobile Safari/537.36"}
    r = get_html(url, headers)
    html = BeautifulSoup(r, "html.parser")

    con = html.find_all("div", class_="one-cita")[0].string
    # print(con)
    day = html.find_all("p", class_="dom")[0].string
    may = html.find_all("p", class_="may")[0].string
    time = day +"  "+ may
    con = con.strip()
    article = time + "->" + con
    print(article)
#     f.write(con)
# f.close()








