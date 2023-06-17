import scrapy


class ExampleSpider(scrapy.Spider):
    # 爬虫名称：爬虫文件唯一标识：可以使用该变量的值来定位到唯一的一个爬虫文件
    name = "data_analysis"
    # 允许的域名：scrapy只可以发起百度域名下的网络请求
    # allowed_domains = ["spider_blood.com"]
    # 起始的url列表：列表中存放的url可以被scrapy发起get请求
    start_urls = ['https://www.jokes8.com/']

    def parse(self, response):
        #如何获取响应数据
        #调用xpath方法对响应数据进行xpath形式的数据解析
        li_list = response.xpath('//*[@id="div_content"]')
        for li in li_list:
            print(li)
            # content = li.xpath('./div[1]/text()')[0]
            # title = li.xpath('./div[2]/a/text()')[0]
            # #&lt;Selector xpath='./div[2]/a/text()' data='一年奔波，尘缘遇了谁'&gt;
            # print(title)#selector的对象，且我们想要的字符串内容存在于该对象的data参数里
            #解析方案1：
            # title = li.xpath('./div[2]/a/text()')[0]
            # content = li.xpath('./div[1]/text()')[0]
            # #extract()可以将selector对象中data参数的值取出
            # print(title.extract())
            # print(content.extract())
            #解析方案2：
            #title和content为列表，列表只要一个列表元素
            # title = li.xpath('./article/div[1]/h2/a/text()')
            # print(title.extract_first())
            # title = li.xpath('./div[2]/a/text()')
            # content = li.xpath('./div[1]/text()')
            # #extract_first()可以将列表中第0个列表元素表示的selector对象中data的参数值取出
            # print(title.extract_first())
            # print(content.extract_first())