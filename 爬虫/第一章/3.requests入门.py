# coding: utf-8 
# @Time    : 2022/10/8 下午9:50
#安装requsts
#pip install requests
#国内源 清华源 阿里源
import requests
query = input("请输入一个明星:")
url = 'https://www.sogou.com/web?query={}'.format(query)
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}
resp = requests.get(url,headers=headers) #headers  处理反爬
print(resp)
# print(resp.text) ##拿到页面源代码
