import  requests


# 请求参数动态化
keyword = input("请输入关键字:")

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

params = {
    'query': keyword
}
url = 'https://www.sogou.com/web'

response = requests.get(url=url,params=params,headers=headers)
print(response.text)

fileName = keyword +'.html'
with open(fileName,'w',encoding='utf-8') as fp:
    fp.write(response.text)