import requests
from lxml import etree

# 请求头------------------------------------------------------------------------------------------------------------
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 '
                  'Safari/537.36'}


def get_url():
    for i in range(10):
        url = 'https://book.douban.com/top250?start={}'.format(i * 25)
        url_data(url)


def url_data(url):
    html = requests.get(url, headers=headers).text
    res = etree.HTML(html)
    # trs = res.xpath('//*[@id="content"]/div/div[1]/div/table/tr')
    trs = res.xpath('//*[@id="content"]/div/div[1]/div/table[2]')
    for tr in trs:
        name = tr.xpath('./tbody/tr/td[2]/div[1]/a/text()')
        comment = tr.xpath('./tbody/tr/td[2]/p[2]/span/text()')[0].replace('(', '').replace(')', '').strip()
        info = tr.xpath('./tbody/tr/td[2]/p[1]/text()')
        book_image = tr.xpath('./tbody/tr/td[1]/a/img/@src')
        print("《{}》--{}--{}--{}".format(name, comment, info,book_image))

get_url()
