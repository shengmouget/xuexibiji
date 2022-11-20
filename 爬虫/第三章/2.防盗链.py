# coding: utf-8 
# @Time    : 2022/10/10 下午5:41
# 拿到contId
# 拿到videoStatus返回的json
# srcUrl里面的内容修改
# 下载视频
import requests
url = 'https://www.pearvideo.com/video_1148699'
contId = url.split('_')[1]
videoStatusurl = f'https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.5471478813519184'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    # 防盗链 反扒  溯源 当前请求的上一级
    'Referer': url
}
resp = requests.get(videoStatusurl,headers=headers)
dic = resp.json()
srcUrl = dic["videoInfo"]['videos']['srcUrl']
systemTime = dic['systemTime']
srcUrl = srcUrl.replace(systemTime,f'cont-{contId}')
with open('a.mp4','wb') as f:
    f.write(requests.get(srcUrl).content)
resp.close()
# https://video.pearvideo.com/mp4/short/20170905/cont-1148699-10845498-hd.mp4
# https://video.pearvideo.com/mp4/short/20170905/1665412955032-10845498-hd.mp4