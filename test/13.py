import urllib.request
import re
keyname="连衣裙"
key=urllib.request.quote(keyname)
headers = ("User-Agent", "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0")
opener=urllib.request.build_opener()
opener.addheaders=[headers]
urllib.request.install_opener(opener)
for i in range(1,10):
    print("第"+str(i)+"次")
    url="https://s.taobao.com/list?q="+key+"&cat=16&style=grid&seller_type=taobao&spm=a219r.lm874.1000187.1&bcoffset=12&s="+str(i*60)
    data=urllib.request.urlopen(url).read().decode("utf-8","ignore")
    pat='pic_url":"//(.*?)"'
    imagelist=re.compile(pat).findall(data)
    for j in range(0,len(imagelist)):
        thisimg=imagelist[j]
        thisimgurl="http://"+thisimg
        file="F:/demo/"+str(i)+str(j)+".jpg"
        urllib.request.urlretrieve(thisimgurl,filename=file)
    print("ok")