# coding: utf-8 
# @Time    : 2022/10/12 下午10:07
# 一般的视频网站工作原理：
# 用户上传 ->  转码 （把视频做处理 2K 1080 标清） ->切片处理 （把单个文件进行拆分）
# 用户在进行拉动进度条的时候
# 需要一个文件记录：1.视频播放顺序 2.视频存放的路径
# 把拆分好的视频放在 M3U txt  json -->文本


# 想要抓取一个视频  找到m3u8   通过m3u8 下载ts文件
# 通过各种手段（不仅是编程手段 ） 把ts文件合并为一个mp4文件
import requests
from lxml import etree

url = 'https://www.lagou.com/wn/jobs?labelWords=&fromSearch=true&suginput=&kd=python'
# heards = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
#     'Referer': 'https://www.lagou.com/utrack/trackMid.html?f=https%3A%2F%2Fwww.lagou.com%2Fwn%2Fjobs%3FlabelWords%3D%26fromSearch%3Dtrue%26suginput%3D%26kd%3Dpython&t=1665677574&_ti=1'
# }
resp = requests.get(url)
resp.encoding = 'UTF-8'
print(resp.text)
