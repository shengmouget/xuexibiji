import scrapy

class FirstSpider(scrapy.Spider):
    # 爬虫文件的名称  就是爬虫源文件的唯一标识
    name = 'first'
    # 允许的域名
    # allowed_domains = ['www.xxx.com']
    # 起始的url列表：该列表中存放的url会被scrapy自动进行请求的发送
    start_urls = ['https://www.baidu.com/','https://www.sogou.com/']

    # 用作数据解析：response参数表示的就是请求成功后对应的响应
    def parse(self,response):
        print(response)
