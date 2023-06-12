import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/97.0.4692.71 Safari/537.36'
}
url = "https://ip.900cha.com/"

# proxies = {"代理类型": "ip:port"}
proxies = {"https": "49.89.126.72:4231"}
result = requests.get(url=url, headers=headers, proxies=proxies).text
tree = etree.HTML(result)
li = tree.xpath('//*[@class="list-unstyled"]/li[1]/text()')[0]
print(li)
