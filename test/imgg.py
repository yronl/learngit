#__author__:YR
#__info__:None

import requests
from bs4 import BeautifulSoup
from lxml import etree

url = "http://www.daqo.com/"
headers = {"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Mobile Safari/537.36"}
r = requests.get(url, headers=headers)
count=[]
soup=BeautifulSoup(r.text,"lxml")
for item in soup.select(".ColorC"):
    for img in item.find_all("img"):
        print("img", img)
        img_path = img.get("src")
        count.append(img_path)
for i,v in enumerate(count):
    image = requests.get(v)
    with open("f:\\img"+str(i)+".jpg","wb")as file:
        file.write(image.content)
        file.close()