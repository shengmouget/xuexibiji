# coding: utf-8 
# @Time    : 2022/10/11 下午11:16
import bs4
import requests
import re
import re
url = 'http://book.sbkk8.com/gudai/sidawenxuemingzhu/xiyouji/116671.html'
resp = requests.get(url)
resp.encoding = 'gbk'
# print(resp.text)
page_1 = resp.text
obj = re.compile('<h1 class="articleH11">(?P<title>.*?)</h1>',re.S)
tit = obj.finditer(resp.text)
for it in tit:
    title = it.group('title')
page_html = bs4.BeautifulSoup(page_1,"html.parser")
plist = page_html.find('div',id="content").find_all('p')
text_list = []
for a in plist:
    text_list.append(a)
text_list = str(text_list)
text_list = text_list.translate(str.maketrans({'<':None,'p':None,'>':None,'/':None}))\
    .replace('u一u','').replace('[','').replace(']','')
with open('/Users/mac/Desktop/image_test/' + title + '.txt','w') as file:
    file.write(text_list)