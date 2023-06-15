import scrapy


class ExampleSpider(scrapy.Spider):
    # 爬虫名称：爬虫文件唯一标识：可以使用该变量的值来定位到唯一的一个爬虫文件
    name = "spider_blood"
    # 允许的域名：scrapy只可以发起百度域名下的网络请求
    # allowed_domains = ["spider_blood.com"]
    # 起始的url列表：列表中存放的url可以被scrapy发起get请求
    start_urls = ["https://www.baidu.com/","https://www.authing.cn/"]

    # 专门用作于数据解析
    # 参数response：就是请求之后对应的响应对象
    # parse的调用次数，取决于start_urls列表元素的个数
    def parse(self, response):
        print('响应对象为：', response)
