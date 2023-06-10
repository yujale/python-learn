import requests
import re
from urllib import request

# 使用正则爬取图片资源
url = "http://md.itlun.cn/a/nhtp/"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/114.0.0.0 Safari/537.36"
}

response = requests.get(url=url,headers=headers)
response.encoding= 'gbk'
result = response.text
## 数据解析
ex = '<script.*?src = "(.*?)"; </script>';
img_src_list = re.findall(ex,result,re.S)

for  img_src in img_src_list:
    img_src = "http:"+img_src
    img_name = img_src.split( '/')[-1]
    request.urlretrieve(img_src, img_name)
    print(img_name, '下载成功')



