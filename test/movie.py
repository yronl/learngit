#__author__:YR
#__info__:None
#豆瓣电影词云

from urllib import request
from bs4 import BeautifulSoup
import re
import jieba
import pandas as pd
import numpy
import matplotlib.pyplot as plt
import matplotlib
from wordcloud import WordCloud
%matplotlib inline


resp = request.urlopen("https://movie.douban.com/cinema/nowplaying/zhuzhou/")
html_data = resp.read().decode("utf-8")
html = BeautifulSoup(html_data, "html.parser")
nowplaying_movie = html.find_all("div", id='nowplaying')
nowplaying_movie_list = nowplaying_movie[0].find_all("li", class_="list-item")

nowplaying_list = []
for item in nowplaying_movie_list:
    nowplaying_dict = {}
    nowplaying_dict['id'] = item['data-subject']
    for tag_img_item in item.find_all('img'):
        nowplaying_dict['name'] = tag_img_item['alt']
        nowplaying_list.append(nowplaying_dict)

requrl = 'https://movie.douban.com/subject/'+nowplaying_list[0]['id']+'/comments' +'?' +'start=0' + '&limit=20'
resp = request.urlopen(requrl)
html_data = resp.read().decode("utf-8")
html = BeautifulSoup(html_data, "html.parser")
comment_div_lits = html.find_all('div', class_='comment')
eachCommentlist = []
for item in comment_div_lits:
    if item.find_all('p')[0].string is not None:
        eachCommentlist.append(item.find_all('p')[0].string)

comments = ''
for k in range(len(eachCommentlist)):
    comments = comments + (str(eachCommentlist[k])).strip()

# 数据清洗
pattern = re.compile(r'[\u4e00-\u9fa5]+')
filterdata = re.findall(pattern, comments)
cleaned_comment = ''.join(filterdata)

# 中文分词操作
segment = jieba.lcut(cleaned_comment)
words_df = pd.DataFrame({'segment': segment})
stopwords = pd.read_csv('stopwords.txt', index_col=False, quoting=3, sep='\t', names=['stopword'], encoding="gbk")
words_df = words_df[~words_df.segment.isin(stopwords.stopword)]
words_df.head()


# 词频统计
words_stat = words_df.groupby(by=['segment'])['segment'].agg({"计数" : numpy.size})
words_stat = words_stat.reset_index().sort_values(by=["计数"], ascending=False)

matplotlib.rcParams['figure.figsize'] = (10.0, 5.0)
from wordcloud import WordCloud  # 词云包

wordcloud = WordCloud(font_path="simhei.ttf", background_color="white", max_font_size=80)  # 指定字体类型、字体大小和字体颜色
word_frequence = {x[0]: x[1] for x in words_stat.head(1000).values}
word_frequence_list = []
for key in word_frequence:
    temp = (key, word_frequence[key])
    word_frequence_list.append(temp)

wordcloud = wordcloud.fit_words(word_frequence_list)
plt.imshow(wordcloud)

