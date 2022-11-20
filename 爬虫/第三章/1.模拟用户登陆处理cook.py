# coding: utf-8 
# @Time    : 2022/10/10 下午5:00
# 登陆 -》 得到cookie
# 带着cookie去请求得到url -》书架上的内容

# 必需得上面的两个操作连起来
# 我们可以使用session进行请求 -》 session可以认为是一连串的请求，在这个过程中cookie不会丢
import requests
# 会话
session = requests.session()
# 1 登陆
# url = 'https://gulixueyuan.com/partner/login'
# data = {
#     '_username': '17671148982',
#     '_password': 'shengwei20001112',
#     # '_remember_me': 'on',
#     # '_target_path': '/partner/logout?userId=96496&goto=https%3A%2F%2Fgulixueyuan.com%2Flogin',
#     # '_csrf_token': 'CinWiSQhNrMq6LeeIGSmxd4GFJidcZUltMUHbxpIzNE'
# }
# resp = session.post(url,data=data)
# print(resp.text)

