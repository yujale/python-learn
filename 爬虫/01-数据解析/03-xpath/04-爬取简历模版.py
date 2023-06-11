from lxml import etree
import requests
import os

headers: dict[str, str] = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/97.0.4692.71 Safari/537.36'
}
dirName = '简历'
if not os.path.exists(dirName):
    os.mkdir(dirName)

url = 'https://sc.chinaz.com/jianli/free_%d.html'

for i in range(1, 6):
    if i == 1:
        new_url = 'https://sc.chinaz.com/jianli/free.html'
    else:
        new_url = format(url % i)
    print("----------正在请求下载第%d页的简历数据----------" % i)
    response = requests.get(url=new_url, headers=headers)
    response.encoding = 'utf-8'
    result = response.text
    tree = etree.HTML(result)
    div_list = tree.xpath('//*[@id="container"]/div')
    for div in div_list:
        title = div.xpath('./p/a/text()')[0] + '.rar'
        detail_url = div.xpath('./p/a/@href')[0]
        response = requests.get(url=detail_url, headers=headers)
        response.encoding = 'utf-8'
        detail_page_text = response.text
        # 数据解析：下载地址
        tree = etree.HTML(detail_page_text)
        download_url = tree.xpath('//*[@id="down"]/div[2]/ul/li[1]/a/@href')[0]
        # 在下载请求建立模板
        data = requests.get(url=download_url, headers=headers).content
        img_path = dirName + '/' + title
        with open(img_path, 'wb') as fp:
            fp.write(data)
        print(img_path, "保存下载成功！")
