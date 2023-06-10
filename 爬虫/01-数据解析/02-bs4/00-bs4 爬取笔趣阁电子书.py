from bs4 import BeautifulSoup
import requests

url = 'https://www.gl518.net/book/2782/'

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/114.0.0.0 Safari/537.36"
}

response = requests.get(url=url, headers=headers)
response.encoding = 'utf-8'
result = response.text
soup = BeautifulSoup(result,"html.parser")
# a_list =soup.find('div',name='listmain')
a_list = soup.select('.listmain > dl')
fp = open('./sanguo.txt','w',encoding='utf-8')
for a in a_list:
    print(a)

    # title = a.string
    # detail_url = a['href']
    # detail_url= detail_url[11:len(detail_url)]
    # print(detail_url)
    # if detail_url == 'javascript:dd_show()':
    #     continue
    # detail_url = url + detail_url
    # # 获取章节内容
    # response = requests.get(url=detail_url, headers=headers)
    # response.encoding = 'utf-8'
    # result = response.text
    # soup = BeautifulSoup(result, features="html")
    # div_tag = soup.find('div', id='chaptercontent')
    # content = div_tag.text
    # fp.write(title + '\n' + content + '\n')
    # print(content)
    # print(title, '爬取保存成功')
# fp.close()





