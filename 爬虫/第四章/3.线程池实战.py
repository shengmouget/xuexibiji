# coding: utf-8 
# @Time    : 2022/10/11 下午4:27
from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor
from lxml import etree
import requests
import csv
file = open("data.csv",'a')
csvwriter = csv.writer(file)


def download_one_page(url):
    # 拿到源代码
    requ = requests.get(url)
    requ.encoding = 'gb2312'
    html = etree.HTML(requ.text)
    tables = html.xpath('/html/body/div[2]/div[2]/table[1]/tbody/tr')
#     拿到每个tr
    for tr in tables:
        txt = tr.xpath('./td/text()')
        name = tr.xpath('./td[2]/a/text()')[0]
        txt.insert(1,name)
        txt = [item.strip('\xa0') for item in txt]
        csvwriter.writerow(txt)
    print(url,'提取完毕')




if __name__ == '__main__':
    # url = 'http://210.30.64.45/dsxx/index.asp?page=1&s_dept_id=0&spid=0&s_user_name=&s_dslb='
    # download_one_page(url)
    with ThreadPoolExecutor(10) as t:
        for i in range(1,10):
            t.submit(download_one_page,f"http://210.30.64.45/dsxx/index.asp?page={i}&s_dept_id=0&spid=0&s_user_name=&s_dslb=")

    print("over")