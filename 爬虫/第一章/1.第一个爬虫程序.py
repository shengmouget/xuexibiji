# coding: utf-8 
# @Time    : 2022/10/8 下午8:49
from urllib.request import urlopen

url = 'http://www.baidu.com'
resp = urlopen(url)

with open('/Users/mac/Desktop/bug/mybaidu.html','w',encoding='utf-8') as file:
    file.write(resp.read().decode('utf-8')) #decode 解码
print('over')