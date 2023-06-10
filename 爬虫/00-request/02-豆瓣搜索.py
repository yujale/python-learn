import requests

url = 'https://movie.douban.com/j/chart/top_list'

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

params = {
    "type": "11",
    "interval_id": "100:90",
    "action": "",
    "start": " 0",
    "limit": "20"
}

response = requests.get(url=url, headers=headers, params=params)

result = response.json()
fp =  open('./douban.text','w',encoding='utf-8')
print(result)
for dic in result:
    title = dic['title']
    score = dic['score']
    fp.write(title+ score)
    print(title, '爬虫保存成功！')
