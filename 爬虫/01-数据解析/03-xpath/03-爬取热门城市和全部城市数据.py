from lxml import etree
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/97.0.4692.71 Safari/537.36'
}

url = 'https://www.aqistudy.cn/historydata/'

response = requests.get(url=url, headers=headers)
result = response.text

tree = etree.HTML(result)
# 写法一
hot_li_list = tree.xpath('//div[@class="bottom"]/ul/li')
for hot in hot_li_list:
    city_name = hot.xpath('./a/text()')[0]
    print(city_name)

all_li_list = tree.xpath('//div[@class="bottom"]/ul/div[2]/li')
for li in all_li_list:
    city_name = li.xpath('./a/text()')[0]
    print(city_name)

# #解析热门城市+所有城市
# #此处xpath表达式的管道符（|）可以是的xpath表达式更加具有通用性
li_list = tree.xpath('//div[@class="bottom"]/ul/li | //div[@class="bottom"]/ul/div[2]/li')
for li in li_list:
    city_name = li.xpath('./a/text()')[0]
    print(city_name)


