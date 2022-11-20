# coding: utf-8 
# @Time    : 2022/10/9 下午9:06
import csv
import requests
"""
{'id': 1344795, 'prodName': '大白菜', 'prodCatid': 1186, 
'prodCat': '蔬菜', 'prodPcatid': None, 'prodPcat': '', 
'lowPrice': '0.8', 'highPrice': '0.9', 'avgPrice': '0.85',
 'place': '冀', 'specInfo': '', 'unitInfo': '斤', 
 'pubDate': '2022-10-09 00:00:00', 
 'status': None, 'userIdCreate': 138, 'userIdModified': None, 'userCreate': 'admin',
 'userModified': None, 'gmtCreate': None, 'gmtModified': None}
"""
url = 'http://www.xinfadi.com.cn/getPriceData.html'
file = open('price.csv','w')
csv_pan = csv.writer(file)
resp = requests.post(url)
resp_list = resp.json()['list']
for it in resp_list:
    csv_pan.writerow(it.values())
print('over')
file.close()
resp.close()




