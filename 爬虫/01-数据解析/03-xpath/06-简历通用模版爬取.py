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

# 通用的url模板
url = "https://sc.chinaz.com/jianli/free_%d.html"
for page in range(1, 11):
    if page == 1:
        new_url = "https://sc.chinaz.com/jianli/free.html"
    else:
        new_url = format(url % page)
    response = requests.get(url=new_url, headers=headers)
    response.encoding = "utf-8"
    page_text = response.text
    # 数据解析：详情页url和简历名称
    tree = etree.HTML(page_text)
    div_list = tree.xpath('//*[@id="container"]/div')
    # 局部解析
    for div in div_list:
        detail_url = "https:" + div.xpath("./a/@href")[0]
        title = div.xpath("./p/a/text()")[0] + ".rar"
        # 对详情页的url发起请求，解析出简历的下载地址
        detail_page_text = requests.get(url=detail_url, headers=headers).text
        # 数据解析：解析下载地址
        detail_tree = etree.HTML(detail_page_text)
        li_list = detail_tree.xpath('//*[@id="down"]/div[2]/ul/li')
        down_list = []  # 存储不同的12个下载地址
        for li in li_list:
            download_link = li.xpath("./a/@href")[0]
            down_list.append(download_link)
        # 随机选择一个下载地址进行简历模板的下载
        import random

        # 从列表中随机选出一个下载地址
        link = random.choice(down_list)
        # 对下载地址进行请求发送，下载简历模板的压缩包
        data = requests.get(url=link, headers=headers).content
        filePath = dirName + "/" + title
        with open(filePath, "wb") as fp:
            fp.write(data)
        print(title, "下载保存成功！")
