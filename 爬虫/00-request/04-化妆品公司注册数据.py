import requests
import time

url = 'https://www.nmpa.gov.cn/datasearch/data/nmpadata/search'
print(int(time.time()))
params = {
    "itemId": "ff8080818046502f0180f934f6873f78",
    "isSenior": "N",
    "searchValue": "美",
    "pageNum": 1,
    "pageSize": 10,
    "timestamp": int(time.time())
}

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/114.0.0.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*"
}

response = requests.get(url=url, headers=headers, params=params)
print(response.text)
#
# result = response.json()
# print(result)
