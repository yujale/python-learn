from lxml import etree
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/97.0.4692.71 Safari/537.36'
}
url = "http://slide.photo.sina.com.cn/"
response = requests.get(url=url,headers=headers)
response.encoding = "gbk"
page_text = response.text
print(page_text)
#数据解析：图片地址+标题
tree = etree.HTML(page_text)
#直接删除被隐藏的div，将其在xpath表达式中跨过即可
li_list = tree.xpath('//*[@id="eData"]/dl')
for li in li_list:
    title = li.xpath("./h3")[0]
    img_src = li.xpath('./dd[1]')[0]
    print(img_src,title)
