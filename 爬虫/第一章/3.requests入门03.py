# coding: utf-8 
# @Time    : 2022/10/8 下午10:27
import requests
import openpyxl
wk = openpyxl.Workbook()
sheet = wk.create_sheet()
url = 'https://movie.douban.com/j/chart/top_list'
#重新封装参数
param = {
    'type': '24',
    'interval_id': '100:90',
    'action':'',
    'start': 20,
    'limit': 40
}
header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}
requ = requests.get(url,params=param,headers = header)
js = requ.json()
for item in js:
    title = item['title']
    score = item['score']
    actors = item['actors'][0]
    regions = item['regions'][0]
    types = str(item['types']).replace('\'','').replace('[','').replace(']','')
    sheet.append([title,score,regions,actors,types])
    wk.save('/Users/mac/Desktop/image_test/01.xlsx')
requ.close()





