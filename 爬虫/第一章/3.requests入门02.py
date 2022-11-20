# coding: utf-8 
# @Time    : 2022/10/8 下午10:18
import requests
url = 'https://fanyi.baidu.com/sug'
s = input('请输入要翻译的单词')
dat = {
    'kw': s
}

#发送post请求 发送的数据必需放在字典中，通过data来传送
requ = requests.post(url,data=dat)
print(requ.json()) #将服务器返回的内容直接处理成json
