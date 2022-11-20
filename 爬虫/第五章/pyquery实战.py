# coding: utf-8 
# @Time    : 2022/10/15 下午10:15
# 汽车之家

import requests
def get_page_text(url):
    resq = requests.get(url)



def main():
    url = 'https://k.autohome.com.cn/146'
#     提取页面源代码
    html = get_page_text(url)
#     解析 提取数据


if __name__ == '__main__':
    main()