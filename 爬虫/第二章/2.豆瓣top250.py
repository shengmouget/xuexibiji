# coding: utf-8 
# @Time    : 2022/10/9 下午4:42
#拿到网页源代码
#通过正则re来提取有效信息
import requests
import re
import csv

url = 'https://movie.douban.com/top250'
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}
resp = requests.get(url,headers=headers)
page_content = resp.text

#解析数据
obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)'
                 r'</span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp'
                 r'.*?<span class="rating_num" property="v:average">'
                 r'(?P<score>.*?)</span>.*?<span>(?P<num>.*?)人评价</span>',re.S)
result = obj.finditer(page_content)
file = open('data.csv','w')
csvwriter = csv.writer(file)
for it in result:
    dic = it.groupdict()
    dic['year'] = dic['year'].strip()
    csvwriter.writerow(dic.values())
    # print(it.group('name'))
    # print(it.group('year').strip())
    # print(it.group('num'))
    # print(it.group('score'))
resp.close()
print("over")
