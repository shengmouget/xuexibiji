# coding: utf-8 
# @Time    : 2022/10/9 下午5:12
# 网址:https://www.dytt89.com/
# 定位到2022必看片
# 从2022中提取到子页面的链接地址
# 请求子页面的链接地址 拿到我们想要的下载地址
import requests
import re
import csv
file = open('download.csv','w')
csvwriter = csv.writer(file)
domain = 'https://www.dytt89.com/'
resp = requests.get(domain,verify = False)#verify去掉安全验证
resp.encoding = 'gb2312'  #指定字符集
# print(resp.text)
# 拿到ul里面li
obj1 = re.compile(r'2022必看热片.*?<ul>(?P<ul>.*?)</ul>',re.S)
obj2 = re.compile(r"<a href='(?P<href>.*?)'",re.S)
obj3 = re.compile(r'◎片　　名(?P<movie>.*?)<br />.*? <td '
                  r'style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<down>.*?)">',re.S)
result1 = obj1.finditer(resp.text)
child_href_list = []
for it in result1:
    ul = it.group('ul')
    # print(ul)
    #提取子页面链接
    result2 = obj2.finditer(ul)
    for itt in result2:
        child_href = domain + itt.group('href').strip('/')
        child_href_list.append(child_href) #把子页面链接保存在列表

for href in child_href_list:
    child_resp = requests.get(href,verify = False)
    child_resp.encoding = 'gb2312'
    # print(child_resp.text)
    result3 = obj3.finditer(child_resp.text)
    for download in result3:
        dic = download.groupdict()
        csvwriter.writerow(dic.values())
        # movie = download.group('movie')
        # down = download.group('down')
resp.close()




