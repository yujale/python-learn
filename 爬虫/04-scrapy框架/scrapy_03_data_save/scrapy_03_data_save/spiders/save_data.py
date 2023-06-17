import scrapy


class SaveDataSpider(scrapy.Spider):
    name = "save_data"
    allowed_domains = ["www.xxx.com"]
    start_urls = ['https://ishuo.cn/duanzi']

    def parse(self, response):
        # 如何获取响应数据
        # 调用xpath方法对响应数据进行xpath形式的数据解析
        li_list = response.xpath('//*[@id="list"]/ul/li')
        all_data = []  # 爬取到的数据全部都存储到了该列表中
        for li in li_list:
            title = li.xpath('./div[2]/a/text()').extract_first()
            content = li.xpath('./div[1]/text()').extract_first()
            # 将段子标题和内容封装成parse方法的返回
            dic = {
                'title': title,
                'content': content
            }
            all_data.append(dic)

        return all_data
