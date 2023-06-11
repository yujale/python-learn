from lxml import etree
import requests
import os

dirName = 'girls'
# 如果文件夹不存在，则新建，否则不新建
if not os.path.exists(dirName):
    os.mkdir(dirName)
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/97.0.4692.71 Safari/537.36'
}
url = 'http://pic.netbian.com/tupian/31766.html'
response = requests.get(url=url, headers=headers)
response.encoding = 'gbk'
result = response.text

tree = etree.HTML(result)
li_list = tree.xpath('//div[@class="photo-pic"]/a/img')

for li in li_list:
    img_title = li.xpath('@title')[0] + '.jpg'
    img_src = 'https://pic.netbian.com' + li.xpath('@src')[0]
    img_data = requests.get(url=img_src, headers=headers).content
    img_path = dirName + '/' + img_title
    with open(img_path, 'wb') as fp:
        fp.write(img_data)
    print(img_title, '下载保存成功！ ')
