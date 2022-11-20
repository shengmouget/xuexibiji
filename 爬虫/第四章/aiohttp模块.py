# coding: utf-8 
# @Time    : 2022/10/11 下午10:28
import aiohttp
import asyncio
from aiohttp import TCPConnector

urls = [
    'http://kr.shanghai-jiuxin.com/file/2020/0608/00a1286b696f6bbe14631b16a71b0f4d.jpg',
    'http://kr.shanghai-jiuxin.com/file/2020/0608/b4ace8d1657f0a669312702f80ab7717.jpg',
    'http://kr.shanghai-jiuxin.com/file/2020/0218/f4d5cb67cb714e4c3c10b822eba51879.jpg'
]
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}

async def aiodownload(url):
    name = url.rsplit('/',1)[1]
    async with aiohttp.ClientSession(connector=TCPConnector(ssl=False)) as session:
        async with session.get(url,headers=headers) as resp:
    #         请求回来了，写入文件
            with open('/Users/mac/Desktop/image_test/'+name,'wb') as f:
                f.write(await resp.content.read())  #读取内容是异步  需要await挂起
    # s = aiohttp.ClientSession()  #等价<===>requests
    print(name,"搞定")

async def main():
    tasks = []
    for url in urls:
        tasks.append(aiodownload(url))
    await asyncio.wait(tasks)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())