# coding: utf-8 
# @Time    : 2022/10/15 下午11:04

# 抓取微博的评论信息

import requests

def page_text(url,params):
    resq = requests.get(url,params=params)
    return resq.json()

def dic_list(dic):
    comments = dic['data']
    for text in comments:
        text_p = text['text_raw']
        print(text_p)


def main():
    url = 'https://weibo.com/ajax/statuses/buildComments'
    params = {
        'is_reload':1,
        'id':'4824914413226187',
        'is_show_bulletin':2,
        'is_mix':0,
        'count':10,
        'uid':'2656274875'
    }
    # 拿到数据
    dic = page_text(url,params)
    #解析数据
    dic_list(dic)

if __name__ == '__main__':
    main()