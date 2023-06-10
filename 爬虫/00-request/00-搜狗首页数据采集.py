import  requests

url = "https://www.sogou.com/"
response = requests.get(url=url)
print(response.text)
with open('./sogou.html','w',encoding='utf-8') as fp:
    fp.write(response.text)
