import requests

url = "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

data = {
    "cname": "",
    "pid": "",
    "keyword": "武汉",
    "pageIndex": 1,
    "pageSize": 10
}

response = requests.post(url=url, headers=headers, data=data)
result = response.json()
addressList = result['Table1']
for address in addressList:
    storeName = address['storeName']
    addressDetail = address['addressDetail']
    print(storeName + "," + addressDetail)
