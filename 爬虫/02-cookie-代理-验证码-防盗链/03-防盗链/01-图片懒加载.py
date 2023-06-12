import requests
from lxml import etree

url = 'https://sc.chinaz.com/tupian/meinvtupian.html'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/97.0.4692.71 Safari/537.36'
}

response = requests.get(url=url, headers=headers)
response.encoding = 'utf-8'
result = response.text
print(result)
etree_html = etree.HTML(result)
div = etree_html.xpath('//div[@class="container"][2]/div[2]')[0]
for d in div:
    img_url = d.xpath('./img/@data-original')[0]
    img_title = d.xpath('./img/@alt')[0]
    img_url = 'https:' + img_url
    img_content = requests.get(url=img_url, headers=headers).content
    with open('img/' + img_title + '.jpg', 'wb') as fp:
        fp.write(img_content)
    print('爬取完成')
