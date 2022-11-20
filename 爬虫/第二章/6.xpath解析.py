# coding: utf-8 
# @Time    : 2022/10/9 下午11:17
# xpath 是在xml文档中收缩内容的一门语言
# html是xml的一个子集
# 安装lxml模块
from lxml import etree
import requests
import re
url = 'https://shiyan.zbj.com/search/service/?kw=saas&r=1&nt=3606&fcn=%E7%94%B5%E5%AD%90%E5%95%86%E5%9F%8E%E7%B3%BB%E7%BB%9F'
resp = requests.get(url)
# print(resp.text)
# 解析
html = etree.HTML(resp.text)
divs = html.xpath('//*[@id="__layout"]/div/div[3]/div/div[3]/div[4]/div[1]/div')
obj = re.compile(r'<span>好评:.*?<span class="num">(?P<haopin>.*?)</span>',re.S)
result = obj.finditer(resp.text)
# haopin_list = []
# for it in result:
#     itt = it.group("haopin")
#     haopin_list.append(itt)
# 拿到每一个服务商的div
# divs = html.xpath('//*[@id="__layout"]/div/div[3]/div/div[3]/div[4]/div[1]/div')
# i = 0
# for div in divs:
#     price = div.xpath("./div/div[3]/div[1]/span[1]/text()")[0]
#     title = 'sasa'.join(div.xpath("./div/div[3]/a/text()"))
#     dianmin = div.xpath("./div/a/div[2]/div[1]/div/text()")[0]
#     haopin = div.xpath('./div/div[3]/div[2]/div[1]/span[2]/text()')
#     print(dianmin)
#     print(price)
#     print(title)
#     print(haopin_list[i])
#     i = i+1
