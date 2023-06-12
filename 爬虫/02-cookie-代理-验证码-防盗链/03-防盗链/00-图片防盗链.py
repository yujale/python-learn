from lxml import etree
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/97.0.4692.71 Safari/537.36',
    "Referer": "https://blog.sina.com.cn/",
}
url = "http://blog.sina.com.cn/s/blog_01ebcb8a0102zi2o.html?tj=1"
response = requests.get(url=url, headers=headers)
response.encoding = 'utf-8'
result = response.text
print(result)
tree = etree.HTML(result)
img_src = tree.xpath('//*[@id="sina_keyword_ad_area2"]/div/a/img/@real_src')
for img in img_src:
    data = requests.get(img, headers=headers).content
    with open('./123.jpg', 'wb') as fp:
        fp.write(data)
